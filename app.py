from flask import Flask, request, jsonify, render_template
import logging
from tax_tables import (
    FEDERAL_STANDARD_DEDUCTIONS,
    FEDERAL_TAX_BRACKETS,
    STATE_TAX_INFO,
    SOCIAL_SECURITY_RATE,
    MEDICARE_RATE,
    FUTA_RATE,
    FUTA_WAGE_BASE,
    STATES,
    SUTA_RATES,
    SOCIAL_SECURITY_WAGE_BASE,
    ADDITIONAL_MEDICARE_TAX_RATE,
    ADDITIONAL_MEDICARE_TAX_THRESHOLDS
)

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

def calculate_futa_tax(wages):
    taxable_wages = min(wages, FUTA_WAGE_BASE)
    gross_futa_tax = taxable_wages * FUTA_RATE
    state_credit = taxable_wages * 0.054  # Uniform state credit rate
    net_futa_tax = gross_futa_tax - state_credit
    return max(net_futa_tax, 0)  # Ensure FUTA tax is not negative

def calculate_suta_tax(wages, state):
    suta_rate = SUTA_RATES[state]
    suta_wage_base = STATE_TAX_INFO[state].get("suta_wage_base", FUTA_WAGE_BASE)
    taxable_wages = min(wages, suta_wage_base)
    suta_tax = taxable_wages * suta_rate
    return suta_tax

def calculate_state_income_tax(wages, state, filing_status):
    standard_deduction = STATE_TAX_INFO[state]["standard_deduction"][filing_status]
    taxable_income = max(wages - standard_deduction, 0)
    tax_brackets = STATE_TAX_INFO[state][filing_status]
    state_income_tax = 0
    for bracket in tax_brackets:
        if taxable_income > bracket[1]:
            state_income_tax += (bracket[1] - bracket[0]) * bracket[2]
        else:
            state_income_tax += (taxable_income - bracket[0]) * bracket[2]
            break
    return state_income_tax

def calculate_federal_income_tax(wages, filing_status, dependents, multiple_jobs, other_income, deductions, extra_withholding, other_tax_credits):
    # Map "Single or Married Filing Separately" to "single"
    if filing_status == "single":
        filing_status = "single"
    elif filing_status == "married":
        filing_status = "married"
    elif filing_status == "head_of_household":
        filing_status = "head_of_household"
    
    standard_deduction = FEDERAL_STANDARD_DEDUCTIONS[filing_status]
    
    # Apply multiple jobs adjustment
    if multiple_jobs == 'yes' and dependents.get('two_jobs_checkbox'):
        standard_deduction /= 2
        tax_brackets = [(bracket[0] / 2, bracket[1] / 2, bracket[2]) for bracket in FEDERAL_TAX_BRACKETS[filing_status]]
    else:
        tax_brackets = FEDERAL_TAX_BRACKETS[filing_status]
    
    taxable_income = max(wages + other_income - standard_deduction - deductions, 0)
    
    # Apply dependent credits
    dependent_credit = 0
    if dependents.get('has_dependents') == 'yes':
        dependent_credit += dependents.get('qualifying_children', 0) * 2000
        dependent_credit += dependents.get('other_dependents', 0) * 500

    # Calculate federal tax
    federal_income_tax = 0
    for bracket in tax_brackets:
        if taxable_income > bracket[1]:
            federal_income_tax += (bracket[1] - bracket[0]) * bracket[2]
        else:
            federal_income_tax += (taxable_income - bracket[0]) * bracket[2]
            break
    
    # Apply credits and adjustments
    federal_income_tax = max(federal_income_tax - dependent_credit - other_tax_credits + extra_withholding, 0)

    return federal_income_tax

@app.route('/')
def index():
    return render_template('index.html', states=STATES)

@app.route('/calculate_taxes', methods=['POST'])
def calculate_taxes():
    try:
        data = request.json
        app.logger.debug(f'Received data: {data}')
        wages = float(data['wages'])
        payPeriods = float(data['payPeriods'])
        state = data['state']
        filing_status = data['filing_status']
        dependents = {
            'has_dependents': data.get('dependents'),
            'qualifying_children': int(data.get('qualifyingChildren', 0)),
            'other_dependents': int(data.get('otherDependents', 0)),
            'two_jobs_checkbox': data.get('twoJobsCheckbox', False)
        }
        multiple_jobs = data.get('multipleJobs', 'no')
        other_income = float(data.get('otherIncome', 0.00))
        deductions = float(data.get('deductions', 0.00))
        extra_withholding = float(data.get('extraWithholding', 0.00)) * payPeriods
        other_tax_credits = float(data.get('otherTaxCredits', 0.00))
        employee_exemptions = data['employeeExemptions']
        
        futa_tax = calculate_futa_tax(wages)
        suta_tax = calculate_suta_tax(wages, state)
        federal_income_tax = calculate_federal_income_tax(wages, filing_status, dependents, multiple_jobs, other_income, deductions, extra_withholding, other_tax_credits)
        state_income_tax = calculate_state_income_tax(wages, state, filing_status)
        

        # Calculate Social Security and Medicare taxes
        if employee_exemptions == 'none':
        
            # Update Social Security tax calculation
            social_security_tax = min(wages, SOCIAL_SECURITY_WAGE_BASE) * SOCIAL_SECURITY_RATE

            # Update Medicare tax calculation with additional Medicare tax
            additional_medicare_threshold = ADDITIONAL_MEDICARE_TAX_THRESHOLDS[filing_status]

            if wages > additional_medicare_threshold:
                medicare_tax = (additional_medicare_threshold * MEDICARE_RATE) + ((wages - additional_medicare_threshold) * ADDITIONAL_MEDICARE_TAX_RATE)
                employer_medicare_tax = additional_medicare_threshold * MEDICARE_RATE
            else:
                medicare_tax = wages * MEDICARE_RATE
                employer_medicare_tax = medicare_tax
        
        else:
            social_security_tax = 0
            medicare_tax = 0

        total_employee_taxes = federal_income_tax + social_security_tax + medicare_tax + state_income_tax
        net_income = wages - total_employee_taxes
        
        total_employer_taxes = futa_tax + suta_tax + social_security_tax + medicare_tax
        
        return jsonify({
            'federal_income_tax': federal_income_tax,
            'social_security_tax': social_security_tax,
            'medicare_tax': medicare_tax,
            'employer_medicare_tax' : employer_medicare_tax,
            'state_income_tax': state_income_tax,
            'total_employee_taxes': total_employee_taxes,
            'net_income': net_income,
            'futa_tax': futa_tax,
            'suta_tax': suta_tax,
            'total_employer_taxes': total_employer_taxes
        })
    except KeyError as e:
        app.logger.error(f'Missing required parameter: {e.args[0]}')
        return jsonify({'error': f'Missing required parameter: {e.args[0]}'}), 400
    except Exception as e:
        app.logger.error(f"Error processing request: {e}")
        return jsonify({'error': 'An internal error occurred'}), 500

if __name__ == '__main__':
    app.run(debug=True)
