from django.urls import path

from datastory.views import (

    ArgumentList, ArgumentDetail, ArgumentCreate, ArgumentUpdate, ArgumentDelete, MotivationList, MotivationDetail,
    MotivationCreate, MotivationUpdate, MotivationDelete, AttitudeList, AttitudeDetail, AttitudeCreate, AttitudeUpdate,
    AttitudeDelete, StrategyList, StrategyDetail, StrategyCreate, StrategyUpdate, StrategyDelete, DimensionList,
    DimensionDetail, DimensionCreate, DimensionUpdate, DimensionDelete, DatastoryList, DatastoryDetail, DatastoryCreate,
    DatastoryUpdate, DatastoryDelete

)

urlpatterns = [

    path('argument/',
         ArgumentList.as_view(),
         name="datastory_argument_list_urlpattern"),

    path('argument/<int:pk>/',
         ArgumentDetail.as_view(),
         name="datastory_argument_detail_urlpattern"),

    path('argument/create',
         ArgumentCreate.as_view(),
         name='datastory_argument_create_urlpattern'),

    path('argument/<int:pk>/update/',
         ArgumentUpdate.as_view(),
         name='datastory_argument_update_urlpattern'),

    path('argument/<int:pk>/delete/',
         ArgumentDelete.as_view(),
         name='datastory_argument_delete_urlpattern'),

    path('motivation/',
         MotivationList.as_view(),
         name="datastory_motivation_list_urlpattern"),

    path('motivation/<int:pk>/',
         MotivationDetail.as_view(),
         name="datastory_motivation_detail_urlpattern"),

    path('motivation/create',
         MotivationCreate.as_view(),
         name='datastory_motivation_create_urlpattern'),

    path('motivation/<int:pk>/update/',
         MotivationUpdate.as_view(),
         name='datastory_motivation_update_urlpattern'),

    path('motivation/<int:pk>/delete/',
         MotivationDelete.as_view(),
         name='datastory_motivation_delete_urlpattern'),

    path('attitude/',
         AttitudeList.as_view(),
         name="datastory_attitude_list_urlpattern"),

    path('attitude/<int:pk>/',
         AttitudeDetail.as_view(),
         name="datastory_attitude_detail_urlpattern"),

    path('attitude/create',
         AttitudeCreate.as_view(),
         name='datastory_attitude_create_urlpattern'),

    path('attitude/<int:pk>/update/',
         AttitudeUpdate.as_view(),
         name='datastory_attitude_update_urlpattern'),

    path('attitude/<int:pk>/delete/',
         AttitudeDelete.as_view(),
         name='datastory_attitude_delete_urlpattern'),

    path('strategy/',
         StrategyList.as_view(),
         name="datastory_strategy_list_urlpattern"),

    path('strategy/<int:pk>/',
         StrategyDetail.as_view(),
         name="datastory_strategy_detail_urlpattern"),

    path('strategy/create',
         StrategyCreate.as_view(),
         name='datastory_strategy_create_urlpattern'),

    path('strategy/<int:pk>/update/',
         StrategyUpdate.as_view(),
         name='datastory_strategy_update_urlpattern'),

    path('strategy/<int:pk>/delete/',
         StrategyDelete.as_view(),
         name='datastory_strategy_delete_urlpattern'),

    path('dimension/',
         DimensionList.as_view(),
         name="datastory_dimension_list_urlpattern"),

    path('dimension/<int:pk>/',
         DimensionDetail.as_view(),
         name="datastory_dimension_detail_urlpattern"),

    path('dimension/create',
         DimensionCreate.as_view(),
         name='datastory_dimension_create_urlpattern'),

    path('dimension/<int:pk>/update/',
         DimensionUpdate.as_view(),
         name='datastory_dimension_update_urlpattern'),

    path('dimension/<int:pk>/delete/',
         DimensionDelete.as_view(),
         name='datastory_dimension_delete_urlpattern'),

    path('datastory/',
         DatastoryList.as_view(),
         name="datastory_datastory_list_urlpattern"),

    path('datastory/<int:pk>/',
         DatastoryDetail.as_view(),
         name="datastory_datastory_detail_urlpattern"),

    path('datastory/create',
         DatastoryCreate.as_view(),
         name='datastory_datastory_create_urlpattern'),

    path('datastory/<int:pk>/update/',
         DatastoryUpdate.as_view(),
         name='datastory_datastory_update_urlpattern'),

    path('datastory/<int:pk>/delete/',
         DatastoryDelete.as_view(),
         name='datastory_datastory_delete_urlpattern'),
]
