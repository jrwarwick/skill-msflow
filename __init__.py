import requests
import json
from os.path import dirname, join

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'jrwarwick'

LOGGER = getLogger(__name__)


class MSFlowSkill(MycroftSkill):

    def __init__(self):
        super(MSFlowSkill, self).__init__(name="MSFlowSkill")

    def initialize(self):
        ##validate service??//self.load_data_files(dirname(__file__))
        valid = 1

        summary_intent = IntentBuilder("SummaryIntent")\
            .require("SummaryKeyword").build()
        self.register_intent(summary_intent, self.handle_summary_intent)


    def handle_summary_intent(self, message):       
        flow_trigger_url = self.settings['flow_trigger_url']
        LOGGER.info(flow_trigger_url )
        payload = {'comments':[ {"expiry":"2018-08-01","message":"Some stuff was broken."}, 
                     {"expiry":"2018-08-02","message":"Data not entered on time."}
                   ],
                     "images":["https://upload.wikimedia.org/wikipedia/commons/2/22/Browser_usage_on_wikimedia_pie_chart.png",
                     "https://upload.wikimedia.org/wikipedia/commons/4/4f/ASCII_Code_Chart.svg"
                   ]
                  }

        response = requests.post(flow_trigger_url, data = json.dumps(payload))
        data = {"response": response.reason.replace('OK','OKAY') + " " +
        str(response.status_code)}
        self.speak_dialog("SummaryResponse", data)


def create_skill():
    return MSFlowSkill()
