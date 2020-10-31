# -*- coding: utf-8 -*-
##############################################################################
#   ONAERP un fork du projet open source Odoo V12.
#   Copyright (C) 2019 ONA ITConsulting S.P.R.L, (<info@ona-itconsulting.com>).
###############################################################################
###############################################################################


{
    # Theme information
    'name': "website noble retour",
    'description': """
    """,
    'category': 'Theme',
    'version': '1.0',
    'depends': ['website','website_crm'],

    # templates
    'data': [
        #'views/options.xml',
        #'views/snippets.xml',
		'views/faireundon.xml',
		'views/nouvelles.xml',
		'views/projets.xml',
		'views/adhesion.xml',
		'views/engagement.xml',
		'views/grpd.xml',
		'views/cookies.xml',
		'views/pompesfunebres.xml',
		'views/cocad.xml',
		'views/conditions_dutilisations.xml',
		'views/confidentialite.xml',
        'views/pages.xml',
		#'views/websitestructure.xml',
		'views/apropos.xml',
		'views/cud.xml',
		'views/adherant.xml',
        'security/ir.model.access.csv',
        #'views/backend_view/Member.xml',
    ],
    #qweb data
     'qweb':[
         'views/pages.xml',
     ]
    ,

    # demo pages
    'demo': [
        'views/demo/demo.xml',
        'demo/pages.xml',
    ],

    # Your information
    'author': "polla joel",
    'website': "",
    'sequence':0,
    'application': True,
    'installable':True,
}