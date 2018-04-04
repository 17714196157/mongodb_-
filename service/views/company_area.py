# -*- coding:utf-8 -*-

"""
File Name : 'company_area'.py
Description:
Author: 'weicheng'
Date: '2018/4/2' '下午2:53'
"""
from flask import Blueprint
from flask import request
from flask import jsonify
from flask_restful import Resource
from flask import current_app
from service.models import dbtool

company_area_entry = Blueprint('company_area', __name__)


# 接口
class CompanyArea(Resource):
    def post(self):
        logger = current_app.app_logger
        logger.info("in post CompanyArea")
        result = dbtool.db_area()
        if len(result) != 0:
            res_result = {**{"result": result}}
        else:
            res_result = {**{"result": None}}
        return jsonify(res_result)