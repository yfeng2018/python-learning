# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from constant import job
from lagou import items
from utils import pgs, rds, mytime


class LaGouPipeline(object):

    def __init__(self):
        host = 'localhost'
        nearjob = 'nearjob'
        self.postgres = pgs.Pgs(host=host, port=12432, db_name=nearjob, user=nearjob, password=nearjob)
        self.redis = rds.Rds(host=host, port=12379, db=3, password='redis6379').redis_cli

    def process_item(self, item, spider):
        if isinstance(item, items.LaGouItem):
            position_id = item.get('position_id')
            city_id = item.get('city_id')
            city = item.get('city')
            job_name = item.get('job_name')
            job_salary = item.get('job_salary')
            job_experience = item.get('job_experience')
            job_education = item.get('job_education')
            job_advantage = item.get('job_advantage')
            job_label = item.get('job_label')
            job_description = item.get('job_description')
            post_job_time = item.get('post_job_time')
            companyId = item.get('companyId')
            company_short_name = item.get('company_short_name')
            company_full_name = item.get('company_full_name')
            company_location = item.get('company_location')
            company_latitude = item.get('company_latitude')
            company_longitude = item.get('company_longitude')
            company_index = item.get('company_index')
            company_finance = item.get('company_finance')
            company_industry = item.get('company_industry')
            company_scale = item.get('company_scale')
            company_zone = item.get('company_zone')
            source_from = job.SourceType.lagou.value
            source_url = item.get('source_url')

        return item

    def save(self, type_id):
        sql = 'insert into {0}(position_id,city_id,city,job_name,job_salary,job_experience,job_education,' \
              'job_advantage,job_label,job_description,post_job_time,company_id,company_short_name,' \
              'company_full_name,company_location,company_latitude,company_longitude,company_index,' \
              'company_finance,company_industry,company_scale,company_zone,source_from,source_url,update_time,' \
              'create_time,expired) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,' \
              '%s,%s,%s,%s,%s,%s,%s,%s)'

        return sql.format(job.TableType.get_table(type_id))
