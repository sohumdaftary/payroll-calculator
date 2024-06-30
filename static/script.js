function updateForm() {
    const paymentType = document.getElementById('paymentType').value;
    if (paymentType === 'salary') {
        document.getElementById('salary-fields').style.display = 'block';
        document.getElementById('hourly-fields').style.display = 'none';
    } else {
        document.getElementById('salary-fields').style.display = 'none';
        document.getElementById('hourly-fields').style.display = 'block';
    }
}

function toggleExemptionFields() {
    const parentFields = document.getElementById('parentFields');
    const under18Fields = document.getElementById('under18Fields');
    const employeeExemptions = document.getElementById('employeeExemptions').value;

    if (employeeExemptions === 'parent') {
        parentFields.style.display = 'block';
        under18Fields.style.display = 'none';
    } else if (employeeExemptions === 'under_18') {
        under18Fields.style.display = 'block';
        parentFields.style.display = 'none';
    } else {
        parentFields.style.display = 'none';
        under18Fields.style.display = 'none';
    }
}

async function calculatePayroll() {
    try {
        const paymentType = document.getElementById('paymentType').value;
        const payFrequency = document.getElementById('payFrequency').value;
        const state = document.getElementById('state').value;
        const filingStatus = document.getElementById('filingStatus').value;
        const dependents = document.querySelector('input[name="dependents"]:checked').value;
        const qualifyingChildren = document.getElementById('qualifyingChildren').value || 0;
        const otherDependents = document.getElementById('otherDependents').value || 0;
        const multipleJobs = document.querySelector('input[name="multipleJobs"]:checked').value;
        const twoJobsCheckbox = document.getElementById('twoJobsCheckbox').checked;
        const otherIncome = document.getElementById('otherIncome').value || 0;
        const deductions = document.getElementById('deductions').value || 0;
        const extraWithholding = document.getElementById('extraWithholding').value || 0;
        const otherTaxCredits = document.getElementById('otherTaxCredits').value || 0;
        const employeeExemptions = document.getElementById('employeeExemptions').value;
        const parentCaresForChild = document.getElementById('parentCaresForChild').checked;
        const parentMaritalStatus = document.getElementById('parentMaritalStatus').checked;
        const under18Student = document.getElementById('under18Student').checked;
        const under18Occupation = document.getElementById('under18Occupation').checked;
        const pay2700 = document.getElementById('pay2700').checked;
        const pay1000 = document.getElementById('pay1000').checked;
        const coverFicaTaxes = document.getElementById('coverFicaTaxes').checked;

        let wages;
        if (paymentType === 'salary') {
            const salary = parseFloat(document.getElementById('salary').value);
            const grossPayMethod = document.getElementById('grossPayMethod').value;
            if (grossPayMethod === 'year') {
                wages = salary;
            } else {
                const payPeriods = { "weekly": 52, "bi-weekly": 26, "semi-monthly": 24, "monthly": 12 }[payFrequency];
                wages = salary * payPeriods;
            }
        } else {
            const hours = parseFloat(document.getElementById('hours').value);
            const hourlyRate = parseFloat(document.getElementById('hourlyRate').value);
            const payPeriods = { "weekly": 52, "bi-weekly": 26, "semi-monthly": 24, "monthly": 12 }[payFrequency];
            wages = hours * hourlyRate * payPeriods;
        }

        const payPeriods = { "weekly": 52, "bi-weekly": 26, "semi-monthly": 24, "monthly": 12 }[payFrequency];

        const response = await fetch('/calculate_taxes', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                wages: wages,
                state: state,
                filing_status: filingStatus,
                dependents: dependents,
                qualifyingChildren: parseInt(qualifyingChildren),
                otherDependents: parseInt(otherDependents),
                multipleJobs: multipleJobs,
                twoJobsCheckbox: twoJobsCheckbox,
                otherIncome: parseFloat(otherIncome),
                deductions: parseFloat(deductions),
                extraWithholding: parseFloat(extraWithholding),
                otherTaxCredits: parseFloat(otherTaxCredits), 
                payPeriods: payPeriods,
                employeeExemptions: employeeExemptions,
                parentCaresForChild: parentCaresForChild,
                parentMaritalStatus: parentMaritalStatus,
                under18Student: under18Student,
                under18Occupation: under18Occupation,
                pay2700: pay2700,
                pay1000: pay1000, 
                coverFicaTaxes: coverFicaTaxes
            })
        });

        if (!response.ok) {
            const errorText = await response.text();
            console.error('Error response:', errorText);
            throw new Error(`Server error: ${response.statusText}`);
        }

        const data = await response.json();
        console.log('Received data:', data);

        let periodWages = wages / payPeriods;
        let periodFederalTax = data.federal_income_tax / payPeriods;
        let periodSocialSecurityTax = data.social_security_tax / payPeriods;
        let periodMedicareTax = data.medicare_tax / payPeriods;
        let periodStateIncomeTax = data.state_income_tax / payPeriods;
        let periodEmployeeTotalTaxes = periodFederalTax + periodSocialSecurityTax + periodMedicareTax + periodStateIncomeTax;
        let periodNetIncome = periodWages - periodEmployeeTotalTaxes;

        let periodFutaTax = data.futa_tax / payPeriods;
        let periodSutaTax = data.suta_tax / payPeriods;
        let periodEmployerSocialSecurityTax = data.social_security_tax / payPeriods;
        let periodEmployerMedicareTax = data.employer_medicare_tax / payPeriods;
        let periodEmployerTotalFicaTaxes = periodEmployerSocialSecurityTax + periodEmployerMedicareTax;
        let periodEmployerTotalFutaSutaTaxes = periodFutaTax + periodSutaTax;
        let periodEmployerTotalTaxes = periodEmployerTotalFicaTaxes + periodEmployerTotalFutaSutaTaxes;

        document.getElementById('results').innerHTML = `
            <h2>Results</h2>
            <table style="width: 100%; text-align: left; border-collapse: collapse;">
                <thead>
                    <tr>
                        <th style="border-bottom: 1px solid #ddd; padding: 8px;">Employee Net Take Home Per Pay Period</th>
                        <th style="border-bottom: 1px solid #ddd; padding: 8px;"></th>
                        <th style="border-bottom: 1px solid #ddd; padding: 8px;">Employer Payroll Obligations Per Pay Period</th>
                        <th style="border-bottom: 1px solid #ddd; padding: 8px;"></th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td style="padding: 8px; font-weight: bold;">Gross Pay:</td>
                        <td style="padding: 8px; text-align: right; font-weight: bold;">$${periodWages.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}</td>
                        <td style="padding: 8px; padding-left: 20px;">Social Security Tax:</td>
                        <td style="padding: 8px; text-align: right;">$${periodEmployerSocialSecurityTax.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}</td>
                    </tr>
                    <tr>
                        <td style="padding: 8px; padding-left: 20px;">Federal Income Tax:</td>
                        <td style="padding: 8px; text-align: right;">$${periodFederalTax.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}</td>
                        <td style="padding: 8px; padding-left: 20px;">Medicare Tax:</td>
                        <td style="padding: 8px; text-align: right;">$${periodEmployerMedicareTax.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}</td>
                    </tr>
                    <tr>
                        <td style="padding: 8px; padding-left: 20px;">State Income Tax:</td>
                        <td style="padding: 8px; text-align: right;">$${periodStateIncomeTax.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}</td>
                        <td style="padding: 8px; font-weight: bold; border-top: 1px solid #ddd;">Total FICA Taxes:</td>
                        <td style="padding: 8px; text-align: right; border-top: 1px solid #ddd;font-weight: bold;">$${periodEmployerTotalFicaTaxes.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}</td>
                    </tr>
                    <tr>
                        <td style="padding: 8px; font-weight: bold; border-top: 1px solid #ddd;">Total Income Taxes:</td>
                        <td style="padding: 8px; text-align: right; border-top: 1px solid #ddd; font-weight: bold;">$${(periodFederalTax + periodStateIncomeTax).toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}</td>
                        <td style="padding: 8px; padding-left: 20px;">FUTA:</td>
                        <td style="padding: 8px; text-align: right;">$${periodFutaTax.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}</td>
                    </tr>
                    <tr>
                        <td style="padding: 8px; padding-left: 20px;">Social Security Tax:</td>
                        <td style="padding: 8px; text-align: right;">$${periodSocialSecurityTax.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}</td>
                        <td style="padding: 8px; padding-left: 20px;">SUTA:</td>
                        <td style="padding: 8px; text-align: right;">$${periodSutaTax.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}</td>
                    </tr>
                    <tr>
                        <td style="padding: 8px; padding-left: 20px;">Medicare Tax:</td>
                        <td style="padding: 8px; text-align: right;">$${periodMedicareTax.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}</td>
                        <td style="padding: 8px; font-weight: bold; border-top: 1px solid #ddd;">Total FUTA and SUTA Taxes:</td>
                        <td style="padding: 8px; text-align: right; border-top: 1px solid #ddd;font-weight: bold;">$${periodEmployerTotalFutaSutaTaxes.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}</td>
                    </tr>
                    <tr>
                        <td style="padding: 8px; font-weight: bold; border-top: 1px solid #ddd;">Total FICA Taxes:</td>
                        <td style="padding: 8px; text-align: right; border-top: 1px solid #ddd; font-weight: bold;">$${(periodSocialSecurityTax + periodMedicareTax).toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}</td>
                    </tr>
                    <tr>
                        <td style="padding: 8px; background-color: #e0f7fa; color: black; font-weight: bold;">Net Take Home Pay:</td>
                        <td style="padding: 8px; text-align: right; background-color: #e0f7fa; color: black; font-weight: bold;">$${periodNetIncome.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}</td>
                        <td style="padding: 8px; background-color: #e0f7fa; color: black; font-weight: bold;">Total Employer Taxes:</td>
                        <td style="padding: 8px; text-align: right; background-color: #e0f7fa; color: black; font-weight: bold;">$${periodEmployerTotalTaxes.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}</td>
                    </tr>

                </tbody>
            </table>
        `;

    } catch (error) {
        console.error('Error caught:', error);
        alert(error.message);
    }
}

