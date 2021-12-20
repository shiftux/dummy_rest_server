from flask import Flask
import text_replies
import os
import werkzeug
import json_logging
import logging
import sys

api = Flask(__name__)
api.debug = True

try:
    import googleclouddebugger
    googleclouddebugger.enable(
        breakpoint_enable_canary=True
    )
except ImportError:
    pass

json_logging.init_flask(enable_json=True)
# json_logging.init_request_instrument(api)

# init the logger as usual
logger = logging.getLogger("api-logger")
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))


@api.errorhandler(werkzeug.exceptions.NotFound)
def handle_not_found(e):
    logger.error("trying to access inexisting route!",
                 extra={'props': {"severity": "ERROR"}})
    return "route not found!\n", 404


@api.errorhandler(werkzeug.exceptions.BadRequest)
def handle_bad_request(e):
    logger.error("bad request!", extra={'props': {"severity": "ERROR"}})
    return "bad request!\n", 400


@api.route('/dirk', methods=['GET'])
def get_dirk():
    return text_replies.dirk_reply()


@api.route('/erich', methods=['GET'])
def get_erich():
    return text_replies.erich_reply()


@api.route('/michi', methods=['GET'])
def get_michi():
    return text_replies.michi_reply()


@api.route('/ueli', methods=['GET'])
def get_ueli():
    return text_replies.ueli_reply()


@api.route('/sandro', methods=['GET'])
def get_sandro():
    return text_replies.sandro_reply()


if __name__ == '__main__':
    if os.getenv('RUNNING_ON_K8S') == 'yes':
        api.run(host='0.0.0.0')
    elif os.getenv('RUNNING_IN_DOCKER') == 'yes':
        api.run(host='0.0.0.0')
    else:
        api.run()
