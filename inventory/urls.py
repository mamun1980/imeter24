from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^items/$', 'inventory.views.list_item', name='item-list'),
    url(r'^search/$', 'inventory.views.search_item', name='item-search'),
    url(r'^get-item/(?P<itemnumber>[\w ,\'-]+)/$', 'inventory.views.get_item', name='get-item'),
    url(r'^filter-items/$', 'inventory.views.get_filtered_items', name='filter-items'),
    url(r'^list/$', 'inventory.views.inventory_items', name='inventory-list'),
    # url(r'^item/add/$', 'inventory.views.add_item', name='add-item'),
    url(r'^item/add/$', 'inventory.views.add_new_item', name='add-new-item'),
    url(r'^item/add-another/$', 'inventory.views.add_another_item', name='add-another-item'),
    url(r'^item/delete/$', 'inventory.views.delete_item', name='delete-item'),
    url(r'^item/edit/(?P<itemid>[\w ,\'-]+)/$', 'inventory.views.edit_item', name='edit-item'),
    url(r'^item/view/(?P<itemid>[\w ,\'-]+)/$', 'inventory.views.item_details', name='item-details'),
    url(r'^item/filter/$', 'inventory.views.item_details_filtered', name='item-details-filtered'),

    url(r'^item/comment/add/$', 'inventory.views.add_item_comment', name='add-item-comment'),


    url(r'^unit-measure-list/$', 'inventory.views.list_unit_measue', name='list-inventory-unit-measure'),
    url(r'^unit-measure-list/json/$', 'inventory.views.list_unit_measue_json2'),
    url(r'^unit-measure/add/$', 'inventory.views.add_unit_measue', name='add-inventory-unit-measure'),
    url(r'^unit-measure/edit/(?P<unit_mes_id>\w+)/$', 'inventory.views.edit_unit_measue', name='edit-inventory-unit-measure'),
    url(r'^unit-measure/delete/$', 'inventory.views.delete_unit_measue', name='delete-inventory-unit-measure'),


    url(r'^production-type-list/$', 'inventory.views.list_production_type', name='list-inventory-production-type'),
    url(r'^production-type/add/$', 'inventory.views.add_production_type', name='add-inventory-production-type'),
    url(r'^production-type/edit/(?P<prod_type_id>\w+)/$', 'inventory.views.edit_production_type', name='edit-inventory-production-type'),
    url(r'^production-type/delete/$', 'inventory.views.delete_production_type', name='delete-inventory-production-type'),


    url(r'^custom-designation-list/$', 'inventory.views.list_custom_designation', name='list-custom-designation-type'),
    url(r'^custom-designation/add/$', 'inventory.views.add_custom_designation', name='add-custom-designation-type'),
    url(r'^custom-designation/edit/(?P<cus_des_id>\w+)/$', 'inventory.views.edit_custom_designation', name='edit-custom-designation-type'),
    url(r'^custom-designation/delete/$', 'inventory.views.delete_custom_designation', name='delete-custom-designation-type'),


    url(r'^location-list/$', 'inventory.views.list_location', name='list-inventory-location'),
    url(r'^location/add/$', 'inventory.views.add_location', name='add-inventory-location'),
    url(r'^location/edit/(?P<loc_id>\d+)/$', 'inventory.views.edit_location', name='edit-inventory-location'),
    url(r'^location/delete/$', 'inventory.views.delete_location', name='delete-inventory-location'),

    url(r'^item/reindex/$', 'inventory.views.item_reindex', name='item-reindex'),
    
)