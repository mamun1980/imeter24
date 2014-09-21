PRINTER_TYPE = (
	('dotmatrix', 'Dot Matrix'),
	('laser', 'Laser'),
	('inkjet', 'Ink Jet')
)

PRINTER_STATUS = (
	('active', 'Active'),
	('dead', 'Dead')
)

QUE_TYPE = (
	('email', 'Email'),
	('printer', 'Printer'),
	('fax', 'Fax'),

)

JOB_STATUS = (
	('new', 'New'),
	('inprogress', 'In progress'),
	('error', 'Error'),
	('completed', 'Completed'),
)

SCHEDULE_TYPE = (
	('weekly', 'Weekly'), 
	('daily', 'Daily'), 
	('randomdays', 'Random week days')
)

SEARCH_STATUS = (
	('new', 'New'),
	('inprogress', 'In progress'),
	('completed', 'Completed'),
)