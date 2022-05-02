# -*- coding: utf-8 -*-
{
    "name": "Moyen de paiment",
    "summary": "Ajoute le moyen de paiement aux Facture, ajout du numéro de chèque",
    "version": "0.2",
    "category": "Purchase",
    "author": "Mehdi Tepava",
    'website': "https://www.pacific-erp.com/",
    "license": "LGPL-3",
    "application": False,
    "installable": True,
    "depends": ["account_accountant"],
    "data": [
        "views/payment_register_wizard_view.xml",
        "views/payment_account_view.xml",
        "report/invoice_inherits_report.xml",
        ],
}
