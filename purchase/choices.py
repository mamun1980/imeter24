
RETURN_TYPE = (
	(0, 'Purchase Order'),
	(1, 'Return For Credit'),
	(2, 'Returned damaged Goods'),
	(3, 'Return For Repair'),
	(4, 'Return For Replacement'),
	(5, 'Return For RE-WORK'),
	(6, 'Returned Excessive Qty'),
	(7, 'Returned Wrong Material'),
)

PO_STATUS_ADD = (
	(0, 'New'),
	(1, 'Printed / Emailed'),
	(2, 'Partial Received'),
	(3, 'Received / Completed'),
	(4, 'Accounting Confirmed'),
)
PO_STATUS = (
	(0, 'New'),
	(1, 'Printed / Emailed'),
	(2, 'Partial Received'),
	(3, 'Received / Completed'),
	(4, 'Accounting Confirmed'),
	(5, 'Closed'),
	(6, 'Canceled'),
)

PO_QUE = (
	(0, 'Print'),
	(1, 'Print'),
	(2, 'Fax'),
	(3, 'Email'),
	(4, 'Print & Fax'),
	(5, 'Print & Email'),
	(6, 'Print, Fax & Eamil'),
)

CON_TYPE = (
	('Email', 'Email'),
	('Phone', 'Phone'),
	('Fax', 'Fax'),
)
PR_STATUS = (
	(0, 'Pending'),
	(1, 'Approved'),
	(2, 'Partial Approved'),
	(3, 'Declined'),
	(4, 'On Hold'),
)

PT_STATUS = (
	(0, 'Ordered'),
	(1, 'Partial Received'),
	(2, 'Received'),
)

PL_TYPE = (
	(0, 'Engineering Parts Order'),
	(1, 'Standared Parts Order'),
	(2, 'F.O.B Order'),
	(3, 'Mod Parts Order Std'),
	(4, 'Mod Parts Order Eng'),
)

PL_ORDER_TYPE = (
	(0, 'Prepaid'),
	(1, 'Prepaid & Charge'),
	(2, 'Collect'),
	(3, '3rd Party Billing'),
)

PL_STATUS = (
	(0, 'New'),
	(1, 'Printed'),
	(3, 'Invoiced'),
	(4, 'Archived'),
)
SL_STATUS = (
	(0, 'New'),
	(1, 'Printed'),
	(2, 'Partial Shipped'),
	(3, 'All Shipped'),
	(4, 'Closed'),
)
SL_ITEM_STATUS = (
	(0, 'Pending'),
	(1, 'Partial Shipping'),
	(2, 'Done'),
)
INVOICE_STATUS = (
	(0, 'New'),
	(1, 'Paid'),
	(2, 'On Hold'),
	(3, 'Archived'),
)