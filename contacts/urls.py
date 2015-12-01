from django.conf.urls import patterns, include, url
from haystack.views import SearchView, search_view_factory


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'contacts.views.sc_contact_home', name='sc-contact'),
    url(r'^remove-qout/$', 'contacts.views.remove_qout', name='remove_qout'),
    url(r'^test/$', 'contacts.views.contact_test', name='contact-test'),
    url(r'^auto/$', 'contacts.views.autocomplete', name='sc-sugessions'),
    url(r'^search/$', 'contacts.views.search_contact', name='search-contact'),
    url(r'^list/$', 'contacts.views.contact_list', name='sc-contact-list'),
    url(r'^(?P<cid>\d+)/$', 'contacts.views.sc_contact_view', name='sc-contact-view'),

    url(r'^add/rel/$', 'contacts.views.sc_contact_add_rel', name='sc-contact-add'),
    url(r'^add/rel_item/$', 'contacts.views.sc_contact_add_rel_item', name='sc-contact-add-item'),
    url(r'^add/$', 'contacts.views.sc_contact_add', name='sc-contact-add'),
    url(r'^edit/(?P<pk>\d+)/$', 'contacts.views.contact_edit', name='sc-contact-edit'),
    url(r'^edit/basic/(?P<pk>\d+)/$', 'contacts.views.contact_edit_basic', name='sc-contact-edit-basic'),
    url(r'^get-contact/(?P<pk>\d+)/$', 'contacts.views.get_contact', name='get-contact'),

    url(r'^get-contact/hover/(?P<pk>\d+)/$', 'contacts.views.get_contact_hover', name='get-contact-hover'),

    url(r'^update/$', 'contacts.views.contact_update', name='sc-contact-update'),
    url(r'^profile/update/$', 'contacts.views.profile_update', name='sc-profile-update'),
    
    url(r'^delete/$', 'contacts.views.contact_delete', name='sc-contact-delete'),


    url(r'^profile/$', 'contacts.views.sc_profile', name='sc-profile'),
    
    # url(r'^update/$', 'contacts.views.sc_update', name='sc-update'),
    
    url(r'^phone/$', 'contacts.views.sc_phone_list', name='sc-phone-list'),
    url(r'^phone/add/$', 'contacts.views.contact_phone_add', name='sc-phone-add-ajax'),
    url(r'^phone/edit/(?P<pid>\d+)/$', 'contacts.views.contact_phone_edit', name='sc-phone-edit'),
    url(r'^phone/delete/$', 'contacts.views.sc_phone_delete', name='sc-phone-delete'),

    url(r'^terms/$', 'contacts.views.view_terms', name='sc-term'),
    url(r'^terms/json/$', 'contacts.views.view_terms_json', name='sc-term-json'),
    url(r'^term/add/$', 'contacts.views.term_add', name='sc-term-add-ajax'),
    url(r'^term/edit/(?P<ptid>\d+)/$', 'contacts.views.term_edit', name='sc-term-edit'),
    url(r'^term/delete/$', 'contacts.views.term_delete', name='sc-term-delete-ajax'),

    url(r'^email/add/$', 'contacts.views.contact_email_add', name='sc-email-add-ajax'),
    url(r'^email/edit/(?P<eid>\d+)/$', 'contacts.views.contact_email_edit', name='sc-email-edit'),
    url(r'^email/delete/$', 'contacts.views.sc_email_delete', name='sc-email-delete'),

    url(r'^email-type/$', 'contacts.views.view_email_types', name='sc-email-type-add-ajax'),
    url(r'^email-type/add/$', 'contacts.views.contact_email_type_add', name='sc-email-type-add-ajax'),
    url(r'^email-type/edit/(?P<etid>\d+)/$', 'contacts.views.email_type_edit', name='sc-email-type-edit'),
    url(r'^email-type/delete/$', 'contacts.views.email_type_delete', name='sc-email-type-delete'),

    url(r'^contact-type/$', 'contacts.views.view_contact_types', name='sc-contact-type-add-ajax'),
    url(r'^contact-type/add/$', 'contacts.views.contact_type_add', name='sc-contact-type-add-ajax'),
    url(r'^contact-type/edit/(?P<ctid>\d+)/$', 'contacts.views.contact_type_edit', name='sc-contact-type-edit'),
    url(r'^contact-type/delete/$', 'contacts.views.contact_type_delete', name='sc-contact-type-delete'),

    url(r'^contact-contact-type/add/$', 'contacts.views.contact_contact_type_add', name='contact-contact-type-add-ajax'),
    url(r'^contact-contact-type/edit/(?P<cctid>\d+)/$', 'contacts.views.contact_contact_type_edit', name='contact-contact-type-edit'),
    url(r'^contact-contact-type/delete/$', 'contacts.views.contact_contact_type_delete', name='contact-contact-type-delete'),


    url(r'^delivery-choice/$', 'contacts.views.view_delivery_choices', name='delivery-choice'),
    url(r'^delivery-choice/add/$', 'contacts.views.add_delivery_choices', name='add-delivery-choice'),
    url(r'^delivery-choice/edit/(?P<dcid>\d+)/$', 'contacts.views.edit_delivery_choices', name='edit-delivery-choice'),
    url(r'^delivery-choice/delete/$', 'contacts.views.delivery_choices_delete', name='delete-delivery-choice'),
    url(r'^delivery-choice/list/$', 'contacts.views.list_delivery_choices', name='delivery-choice-list'),

    url(r'^distribution-method/$', 'contacts.views.view_distribution_method', name='distribution-method'),
    url(r'^distribution-method/add/$', 'contacts.views.add_distribution_method', name='add-distribution-method'),
    url(r'^distribution-method/edit/(?P<dmid>\d+)/$', 'contacts.views.edit_distribution_method', name='edit-distribution-method'),
    url(r'^distribution-method/delete/$', 'contacts.views.delete_distribution_method', name='delete-distribution-method'),

    url(r'^contact-distribution-method/add/$', 'contacts.views.contact_distribution_method_add', name='contact-distribution-method-add-ajax'),
    url(r'^contact-distribution-method/edit/(?P<cdmid>\d+)/$', 'contacts.views.contact_distribution_method_edit', name='contact-distribution-method-edit'),
    url(r'^contact-distribution-method/delete/$', 'contacts.views.contact_distribution_method_delete', name='contact-distribution-method-delete'),


    url(r'^currency/$', 'contacts.views.view_currency', name='view-currency'),
    url(r'^currency/json/$', 'contacts.views.get_currencies', name='get-currencies'),
    url(r'^currency/add/$', 'contacts.views.add_currency', name='sc-currency-add'),
    url(r'^currency/edit/(?P<curid>\d+)/$', 'contacts.views.edit_currency', name='sc-currency-edit'),
    url(r'^currency/delete/$', 'contacts.views.delete_currency', name='sc-currency-delete'),

    url(r'^phone-type/$', 'contacts.views.view_phone_type', name='phone-type'),
    url(r'^phone-type/add/$', 'contacts.views.add_phone_type', name='add-phone-type'),
    url(r'^phone-type/edit/(?P<ptid>\d+)/$', 'contacts.views.edit_phone_type', name='edit-phone-type'),
    url(r'^phone-type/delete/$', 'contacts.views.delete_phone_type', name='delete-phone-type'),



    url(r'^comment/add/$', 'contacts.views.contact_comment_add', name='sc-comment-add-ajax'),
    url(r'^comment/edit/(?P<com_id>\d+)/$', 'contacts.views.contact_comment_edit', name='sc-comment-edit'),
    url(r'^comment/delete/$', 'contacts.views.contact_comment_delete', name='sc-comment-delete'),

    
    url(r'make-call/$', 'contacts.views.make_call'),

    url(r'^contact/reindex/$', 'contacts.views.contact_reindex', name='contact-reindex'),
)
