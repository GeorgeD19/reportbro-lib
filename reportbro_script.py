import json
from reportbro import Report, ReportBroError

with open('example.json') as json_file:
    json_data = json.load(json_file)
    report_definition = json_data.get('report')
    output_format = json_data.get('outputFormat')
    if output_format not in ('pdf', 'xlsx'):
        print('outputFormat parameter missing or invalid')
    data = json_data.get('data')
    is_test_data = bool(json_data.get('isTestData'))

try:
    report = Report(report_definition, data, is_test_data)
except Exception as e:
    print('failed to initialize report: ' + str(e))

if report.errors:
    print(dict(errors=report.errors))
try:
    report_file = report.generate_pdf()
except ReportBroError:
    print(dict(errors=report.errors))

f = open("report.pdf", "a")
f.write(report_file)
f.close()