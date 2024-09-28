from django.urls import path
from . import views

urlpatterns = [
    # 模板
    path('', views.index),
    # path('\d+', views.route_params_int),
    path('<int:uid>', views.route_params_int),
    path('<str:name>', views.route_params_str),
    path('<str:name>/<int:version>', views.route_params_multi),
    path('alias/name', views.route_alias, name="alias"),
    path('alias/reflect', views.route_reflect),
    # path('cert/', views.cert),
    # path('personnel/', views.personnel),
    # path('achievement/', views.achievement),
    # path('record/', views.record),
    # path('commerce/', views.commerce),
    #
    # # 注册时间
    # path('api/regtime/count/', views.area_count),
    # # 注册资金
    # path('api/money/count/', views.money_count),
    # # 备案统计
    # path('api/record/count/', views.record_count),
    # # 专业承包
    # path('api/profession_cert/count/', views.profession_cert_count),
    # # 总承包
    # path('api/all_cert/count/', views.all_cert_count),
    # # 勘察
    # path('api/survey_cert/count/', views.survey_cert_count),
    # # 设计
    # path('api/design_cert/count/', views.design_cert_count),
    # # 监理
    # path('api/supervision_cert/count/', views.supervision_cert_count),
    # # 设计与施工一体化资质
    # path('api/integration_cert/count/', views.integration_cert_count),
    # # 招标代理
    # path('api/tender_cert/count/', views.tender_cert_count),
    # # 造价咨询资质
    # path('api/cost_cert/count/', views.cost_cert_count),
    #
    # # 注册人员
    # path('api/data_engineer/count/', views.data_engineer),
    # # 招投标
    # path('api/project_tender_date/count/', views.project_tender_date),
    # # 数据面板
    # path('api/month/', views.DaysList.as_view()),
    #
    # path('api/company/', views.CompanyInfo.as_view()),
]
