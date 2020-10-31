from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import  WebsiteSale


class  WebsiteSaleInherit(WebsiteSale):

    @http.route(['/shop/cart/update'], type='http', auth="public", methods=['POST'], website=True, csrf=False)
    def cart_update(self, product_id, add_qty=1, set_qty=0, **post):

        #description of member data form
        if product_id == 2:

            Members = {
            'subscriber_name': post.get('NomsMembre'),
            'subscriber_first_name': post.get('prenoms'),
            'subscriber_born_at': post.get('bornplace'),
            'subscriber_mobile_phone': post.get('fonesubscriber'),
            'subscriber_professional_phone': post.get('professionalphone'),
            'subscriber_email': post.get('subscriberemail'),
            'subscriber_adress': post.get('subscriberadress'),
            'beneficiary_name': post.get('beneficaireName'),
            'beneficiary_mobile': post.get('Ayantdroitphone'),
            'beneficiary_mail': post.get('AyantdroitMail'),
            'beneficiary_Address': post.get('AyantdroitAdresse'),
            'beneficiary_Remark': post.get('Ayantdroitremarques'),
            'PaiementType': post.get('typeoption'),
            'beneficiary_Reference': post.get('reference'),
            'organisation_Name': post.get('organisationouassociation'),}

        res = super(WebsiteSaleInherit,self).cart_update(product_id, add_qty=1, set_qty=0, **post)
        print("odoo Mates",product_id)
        return res

class AdhesionFormController(http.Controller):
    @http.route('/member/Form', type="http", auth="public", website=True)
    def customFormsubmit(self , **post):

        #members = request.env['noble.members'].sudo().search([]) get list of member

        Members={
            'subscriber_name':post.get('NomsMembre'),
            'subscriber_first_name':post.get('prenoms'),
            'subscriber_born_at':post.get('bornplace'),
            'subscriber_mobile_phone':post.get('fonesubscriber'),
            'subscriber_professional_phone':post.get('professionalphone'),
            'subscriber_email':post.get('subscriberemail'),
            'subscriber_adress':post.get('subscriberadress'),
            'beneficiary_name':post.get('beneficaireName'),
            'beneficiary_mobile':post.get('Ayantdroitphone'),
            'beneficiary_mail':post.get('AyantdroitMail'),
            'beneficiary_Address':post.get('AyantdroitAdresse'),
            'beneficiary_Remark':post.get('Ayantdroitremarques'),
            'PaiementType':post.get('typeoption'),
            'beneficiary_Reference':post.get('reference'),
            'organisation_Name':post.get('organisationouassociation'),
        }

        print("receive Date",Members)

        succes ={'succes':'Votre inscription à été'}
        return http.request.render("website_sale.cart",{})