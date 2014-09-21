STOCK_STATUS_TYPE = (
	('normal', 'Normal'),
	('no-stock', 'No Stock'),
	('labor', 'Labor'),
	('no-charge-labor', 'No Charge Labor'),
	('obsolute', 'Obsolute'),
	('production-hold', 'Production Hold'),
)

PO_STATUS_CHOICES = (
	('new', 'New'),
	('in-progress', 'In progress- Awating Delivery'),
	('received-partial', 'Received Partial'),
	('on-hold', 'On Hold'),
	('closed', 'Closed'),

)

SHOP_STATUS_CHOICES = (
	('new', 'New'),
	('in-progress', 'In Progress'),
	('on-hold', 'On Hold'),
	('completed', 'Completed'),
)