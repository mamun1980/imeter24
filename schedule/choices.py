
DONE_CHOICES = (
	('none', 'None'),
	('scheduled', 'Scheduled'),
	('completed', 'Completed'),
)

STATUS_CHOICE = (
	('new', 'New'),
	('issuetoeng', 'Issued to Eng'),
	('drawingsent', 'Drawings Sent to Customer'),
	('drawingapproved', 'Drawings Approved'),
	('issuetoproduction', 'Issued to Production'),
	('issuetoshipping', 'Issued to Shipping'),
	('shipped', 'Shipped'),
	('issuetoinstallers', 'Issued to Installers'),
	('installed', 'Installation Completed'),
	('completed', 'Completed (Awaiting Invoice)'),
	('invoiced', 'Invoiced'),
	('closed', 'Closed'),
	('cancel', 'Cancelled'),
	('onhold', 'On Hold'),
)