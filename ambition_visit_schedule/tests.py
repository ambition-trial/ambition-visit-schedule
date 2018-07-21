from django.test import TestCase

from .visit_schedules.visit_schedule import visit_schedule
from .visit_schedules.schedule import schedule
from .visit_schedules.schedule_w10 import schedule_w10


class TestVisitSchedule(TestCase):

    def test_visit_schedule_models(self):

        self.assertEqual(
            visit_schedule.death_report_model,
            'ambition_prn.deathreport')
        self.assertEqual(
            visit_schedule.offstudy_model,
            'edc_offstudy.subjectoffstudy')
        self.assertEqual(
            visit_schedule.locator_model,
            'edc_locator.subjectlocator')

    def test_schedule_models(self):
        self.assertEqual(
            schedule.onschedule_model,
            'ambition_prn.onschedule')
        self.assertEqual(
            schedule.offschedule_model,
            'ambition_prn.studyterminationconclusion')
        self.assertEqual(
            schedule.consent_model,
            'ambition_subject.subjectconsent')
        self.assertEqual(
            schedule.appointment_model,
            'edc_appointment.appointment')

        self.assertEqual(
            schedule_w10.onschedule_model,
            'ambition_prn.onschedulew10')
        self.assertEqual(
            schedule_w10.offschedule_model,
            'ambition_prn.studyterminationconclusionw10')
        self.assertEqual(
            schedule_w10.consent_model,
            'ambition_subject.subjectconsent')
        self.assertEqual(
            schedule_w10.appointment_model,
            'edc_appointment.appointment')
