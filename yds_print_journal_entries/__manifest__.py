
{
    'name': 'Print Journal Entries Report',
    'version': '17.0.0.0',
    'category': 'Account',
    'summary': 'Allow to print pdf report of Journal Entries.',
    'description': """
    Allow to print pdf report of Journal Entries.
    journal entry
    print journal entry 
    journal entries
    print journal entry reports
    account journal entry reports
    journal reports
    account entry reports

    
""",
    'author': 'Nadine Abdelfattah',
    'depends': ['base', 'account'],
    'data': [
            'data/paper_format.xml',
            'report/report_journal_entries.xml',
            'report/report_journal_entries_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    # "images": ["static/description/Banner.png"],
}

