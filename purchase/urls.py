from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^add-pr/$', 'purchase.views.add_purchase_request', name='add-purchase-request'),
    url(r'^view-pr/(?P<pk>\d+)/$', 'purchase.views.view_purchase_request', name='view-purchase-request'),
    url(r'^approve-pr/(?P<pk>\d+)/$', 'purchase.views.approve_purchase_request', name='approve-pr'),
    url(r'^declien-pr/$', 'purchase.views.declien_purchase_request', name='declien-pr'),
    url(r'^onhold-pr/$', 'purchase.views.onhold_purchase_request', name='onhold-pr'),
    url(r'^comment-pr/$', 'purchase.views.comment_purchase_request', name='comment-pr'),
    url(r'^list-purchase-requests/$', 'purchase.views.list_purchase_request', name='list-purchase-request'),
    url(r'^list-approved-pr/$', 'purchase.views.list_approved_pr', name='list-approved-pr'),
    url(r'^list-ri/json/$', 'purchase.views.list_ri_json', name='list-ri-json'),
    url(r'^request-item/delete/$', 'purchase.views.request_item_delete', name='ri-delete'),

    url(r'^add-po2/$', 'purchase.views.add_purchase_order', name='add-purchase-order'),
    
    url(r'^generate-po/(?P<po_id>\w+)/$', 'purchase.views.generate_po', name='generate-po'),
    url(r'^preview-generate-po/(?P<po_id>\w+)/$', 'purchase.views.preview_generete_po', name='preview-generate-po'),

    # url(r'^add-po/$', 'purchase.views.add_po', name='add-po'),
    url(r'^po/search/$', 'purchase.views.search_po', name='search-po'),
    url(r'^add-po/$', 'purchase.views.add_new_po', name='add-new-po'),
    url(r'^add-po-email/$', 'purchase.views.add_new_po_and_email', name='add-new-po-email'),
    # url(r'^add-po/$', 'purchase.views.add_new_po', name='add-new-po'),
    url(r'^save-po/$', 'purchase.views.save_po', name='save-po'),
    url(r'^show-draft-po/$', 'purchase.views.show_draft_po', name='draft-po'),
    url(r'^list/$', 'purchase.views.po_list', name='po-list'),
    url(r'^get-po-by-id/(?P<pk>\w+)/$', 'purchase.views.get_po_by_id', name='get-po-by-id'),


    url(r'^list-purchase-orders/$', 'purchase.views.list_purchase_orders', name='list-purchase-orders'),
    url(r'^get-purchase-orders/$', 'purchase.views.get_purchase_orders', name='get-purchase-orders'),
    # url(r'^po-items/$', 'purchase.views.get_purchase_orders', name='get-purchase-orders'),


    url(r'^view/(?P<pk>\w+)/$', 'purchase.views.view_purchase_order', name='view-purchase-order'),
    url(r'^edit/(?P<pk>\w+)/$', 'purchase.views.edit_purchase_order', name='view-purchase-order'),
    url(r'^po-delete/$', 'purchase.views.delete_purchase_order', name='delete-purchase-order'),

    url(r'^po-status-cancel/(?P<pk>\w+)/$', 'purchase.views.cancel_po_status', name='cancel-po-status'),
    url(r'^po-change/$', 'purchase.views.change_po', name='cancel-po'),

    url(r'^get-po-items/(?P<po_id>\w+)/$', 'purchase.views.get_po_items', name='get-purchase-order-items'),

    url(r'^add-po-contact/(?P<po_id>[\w ,\'-]+)/$', 'purchase.views.add_po_contact', name='add-purchase-order-contact'),

    url(r'^po-extra-contact/(?P<po_id>[\w ,\'-]+)/$', 'purchase.views.extra_po_contact', name='add-extra-purchase-order-contact'),
    url(r'^delete-po-contact/$', 'purchase.views.delete_extra_po_contact', name='delete-extra-purchase-order-contact'),

    url(r'^pending-list/$', 'purchase.views.purchase_pending_list', name='purchase-pending-list'),
    url(r'^get-pending-list/$', 'purchase.views.get_pending_list', name='get-pending-list'),
    url(r'^receive-item/(?P<item_id>\d+)/$', 'purchase.views.receive_item', name='receive-item'),
    url(r'^received-list/$', 'purchase.views.purchase_received_list', name='purchase-received-list'),


    url(r'^add-pl/$', 'purchase.views.add_packing_list', name='add-packing-list'),
    url(r'^pl/search/$', 'purchase.views.search_packing_list', name='search-packing-list'),
    url(r'^get-pl/(?P<pl_number>\w+)/$', 'purchase.views.get_packing_list', name='get-packing-list'),
    
    url(r'^view-pl/(?P<id>\w+)/$', 'purchase.views.view_packing_list', name=''),
    url(r'^edit-pl/(?P<id>\w+)/$', 'purchase.views.edit_packing_list', name='edit-packing-list'),
    url(r'^pl-delete/$', 'purchase.views.delete_packing_list', name='delete-packing-list'),
    url(r'^pl-list/$', 'purchase.views.pl_list', name='pl-list'),
    url(r'^packing-list/$', 'purchase.views.packing_list', name='packing-list'),
    url(r'^get-pl-items/(?P<pl_number>\w+)/$', 'purchase.views.get_pl_items', name='get-pl-items'),
    url(r'^get-pl-items/$', 'purchase.views.get_pl_items', name='get-pl-items'),

    url(r'^add-invoice/$', 'purchase.views.add_invoice', name='add-invoice'),
    url(r'^invoice-pdf/(?P<invoice_number>\w+)/$', 'purchase.views.generate_invoice_pdf'),
    url(r'^get-invoices/$', 'purchase.views.get_invoices', name='get-invoices'),
    url(r'^get-invoice-items/$', 'purchase.views.get_invoice_items', name='get-invoice-items'),
    url(r'^invoice-list/$', 'purchase.views.invoice_list', name='invoice-list'),
    url(r'^invoice-view/(?P<invoice_id>\w+)/$', 'purchase.views.invoice_view', name='invoice-list'),
    url(r'^delete-invoice/$', 'purchase.views.delete_invoice', name='delete-invoice'),

    url(r'^add-sl/$', 'purchase.views.add_shipping_list', name='add-shipping-list'),

    url(r'^sl/search/$', 'purchase.views.search_shiping_list', name='search-shiping-list'),
    url(r'^generate-sl/(?P<sl_number>\w+)/$', 'purchase.views.generate_sl', name='generate-sl'),
    url(r'^preview-generate-sl/(?P<sl_number>\w+)/$', 'purchase.views.preview_generete_sl', name='preview-generate-sl'),
    url(r'^generate-pl/(?P<pl_number>\w+)/$', 'purchase.views.generate_pl', name='generate-pl'),
    url(r'^preview-generate-pl/(?P<pl_id>\d+)/$', 'purchase.views.preview_generete_pl', name='preview-generate-pl'),
    url(r'^view-sl/(?P<sl_id>\w+)/$', 'purchase.views.view_shipping_list', name='view-shipping-list'),
    url(r'^edit-sl/(?P<sl_id>\w+)/$', 'purchase.views.edit_shipping_list', name='edit-shipping-list'),
    url(r'^shipping-list/$', 'purchase.views.shipping_list', name='shipping-list'),
    url(r'^sl-list-json/$', 'purchase.views.get_sl_json', name='sl-list-json'),
    url(r'^sl/(?P<sl_id>\w+)/json/$', 'purchase.views.get_sl_json_by_id', name='sl-json'),
    url(r'^sl-item-json/(?P<sl_number>\w+)/$', 'purchase.views.get_sl_item_json', name='sl-item-json'),
    url(r'^sl-item-json/$', 'purchase.views.get_sl_item_json', name='sl-item-json'),
    url(r'^sl-delete/$', 'purchase.views.sl_delete', name='sl-delete'),

    url(r'^deliverinternal-list/$', 'purchase.views.list_deliverinternal', name='list-purchase-deliverinternal'),
    url(r'^deliverinternals/json/$', 'purchase.views.list_deliverinternal_json', name='list-purchase-deliverinternal-json'),
    url(r'^deliverinternal/add/$', 'purchase.views.add_deliverinternal', name='add-purchase-deliverinternal'),
    url(r'^deliverinternal/edit/(?P<id>\d+)/$', 'purchase.views.edit_deliverinternal', name='edit-purchase-deliverinternal'),
    url(r'^deliverinternal/delete/$', 'purchase.views.delete_deliverinternal', name='delete-purchase-deliverinternal'),

    url(r'^po/reindex/$', 'purchase.views.po_reindex', name='po-reindex'),
    url(r'^sl/reindex/$', 'purchase.views.sl_reindex', name='sl-reindex'),
    url(r'^pl/reindex/$', 'purchase.views.pl_reindex', name='pl-reindex'),
)