from edc_visit_schedule import VisitSchedule, site_visit_schedules

from .schedule import schedule
from .schedule_w10 import schedule_w10

visit_schedule = VisitSchedule(
    name='visit_schedule',
    verbose_name='Ambition',
    offstudy_model=f'edc_offstudy.subjectoffstudy',
    death_report_model=f'ambition_prn.deathreport',
    locator_model='edc_locator.subjectlocator',
    previous_visit_schedule=None)

visit_schedule.add_schedule(schedule)

visit_schedule_w10 = VisitSchedule(
    name='visit_schedule_w10',
    verbose_name='Ambition W10',
    offstudy_model=f'edc_offstudy.subjectoffstudy',
    death_report_model=f'ambition_prn.deathreport',
    locator_model='edc_locator.subjectlocator',
    previous_visit_schedule=None)

visit_schedule_w10.add_schedule(schedule_w10)

site_visit_schedules.register(visit_schedule)
site_visit_schedules.register(visit_schedule_w10)
