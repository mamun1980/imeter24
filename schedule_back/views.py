from django.shortcuts import render
from django.http import HttpResponse
from schedule.models import *
from schedule_back.models import *
# Create your views here.

def move_data_to_job_back(request):
	jobs = Job.objects.all()
	import pdb; pdb.set_trace();
	for job in jobs:
		new_job, created = Job_back.objects.get_or_create(job_number=job.job_number)
		if created:
			new_job.cab_designation = job.cab_designation
			new_job.date_opened = job.date_opened
			new_job.date_required = job.date_required
			new_job.status = job.status
			new_job.job_name = job.job_name
			new_job.address_1 = job.address_1
			new_job.customer = job.customer
			new_job.customer_contact_name = job.customer_contact_name
			new_job.customer_contact_phone_number = job.customer_contact_phone_number
			new_job.contact_email = job.contact_email
			new_job.number_of_cabs = job.number_of_cabs
			new_job.description = job.description
			new_job.po_number = job.po_number
			new_job.status_notes = job.status_notes
			new_job.drawing_req_date = job.drawing_req_date
			new_job.drawing_sent_to_customer_date = job.drawing_sent_to_customer_date
			new_job.drawing_approved_date = job.drawing_approved_date
			new_job.eng_comment = job.eng_comment
			new_job.search_string = job.search_string

			new_job.save()

	return HttpResponse("done")


def fix_job_commnet(request):
	comments = Comment.objects.all()
	import pdb; pdb.set_trace();
	for com in comments:
		job = Job.objects.get(job_number=com.job_number)
		comment = Comment_back(job=job)
		comment.job_comment = com.job_comment
		comment.comment_by = com.comment_by
		comment.datetime = com.datetime
		comment.save()
	return HttpResponse("Done")


def fix_job_status(request):
	job_statuses = JobStatus.objects.all()
	import pdb; pdb.set_trace();
	for js in job_statuses:
		job, created = Job_back.objects.get_or_create(job_number=js.job.job_number)
		new_js = JobStatus_back.objects.create(job=job)
		new_js.fixtures_req_by = js.fixtures_req_by
		new_js.fixtures_is_done = js.fixtures_is_done
		new_js.fixtures_comment = js.fixtures_comment
		new_js.wood_shop_req_by = js.wood_shop_req_by
		new_js.wood_shop_is_done = js.wood_shop_is_done
		new_js.wood_shop_req_by_comment = js.wood_shop_req_by_comment
		new_js.machine_shop_req_by = js.machine_shop_req_by
		new_js.machine_shop_is_done = js.machine_shop_is_done
		new_js.machine_shop_req_by_comment = js.machine_shop_req_by_comment

		new_js.welding = js.welding
		new_js.welding_is_done = js.welding_is_done
		new_js.welding_comment = js.welding_comment

		new_js.lacquer = js.lacquer
		new_js.lacquer_is_done = js.lacquer_is_done
		new_js.lacquer_comment = js.lacquer_comment

		new_js.trim_shop_req_by = js.trim_shop_req_by
		new_js.trim_shop_is_done = js.trim_shop_is_done
		new_js.trim_shop_req_by_comment = js.trim_shop_req_by_comment

		new_js.cab_assemply_req_by = js.cab_assemply_req_by
		new_js.cab_assemply_is_done = js.cab_assemply_is_done
		new_js.cab_assemply_req_by_comment = js.cab_assemply_req_by_comment

		new_js.install_date = js.install_date
		new_js.install_is_done = js.install_is_done
		new_js.install_date_comment = js.install_date_comment

		new_js.premier_glass = js.premier_glass
		new_js.premier_glass_is_done = js.premier_glass_is_done
		new_js.premier_glass_comment = js.premier_glass_comment

		new_js.tile_installer = js.tile_installer
		new_js.tile_installer_is_done = js.tile_installer_is_done
		new_js.tile_installer_comment = js.tile_installer_comment

		new_js.misc_del = js.misc_del
		new_js.misc_del_is_done = js.misc_del_is_done
		new_js.misc_del_comment = js.misc_del_comment

		new_js.bill = js.bill
		new_js.bill_is_done = js.bill_is_done
		new_js.bill_comment = js.bill_comment

		new_js.hayward = js.hayward
		new_js.hayward_is_done = js.hayward_is_done
		new_js.hayward_comment = js.hayward_comment

		new_js.glenn = js.glenn
		new_js.glenn_is_done = js.glenn_is_done
		new_js.glenn_comment = js.glenn_comment

		new_js.suren = js.suren
		new_js.suren_is_done = js.suren_is_done
		new_js.suren_comment = js.suren_comment

		new_js.roger = js.roger
		new_js.roger_is_done = js.roger_is_done
		new_js.roger_comment = js.roger_comment

		new_js.matt = js.matt
		new_js.matt_is_done = js.matt_is_done
		new_js.matt_comment = js.matt_comment

		new_js.third_party_install = js.third_party_install
		new_js.third_party_install_is_done = js.third_party_install_is_done
		new_js.third_party_install_comment = js.third_party_install_comment

		new_js.tssa_submitted_date = js.tssa_submitted_date
		new_js.tssa_submitted_date_is_done = js.tssa_submitted_date_is_done
		new_js.tssa_submitted_date_comment = js.tssa_submitted_date_comment

		new_js.safety_test_schedule_date = js.safety_test_schedule_date
		new_js.who_will_test = js.who_will_test
		new_js.test_comment = js.test_comment

		new_js.save()
	return HttpResponse('done')

