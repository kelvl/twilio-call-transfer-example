from flask import Flask, request, url_for
from flask import render_template
from twilio.util import TwilioCapability
import twilio.twiml
from twilio.rest import TwilioRestClient

app = Flask(__name__)

TWILIO_ACCOUNT_SID = "XXXXX"
TWILIO_AUTH_TOKEN = "XXXXX"

# temporary storage for client to call_sid mapping
# we should use a more persistent storage for production
client_to_incoming_sid = {}


@app.route('/transfer_call/<from_client>/to/<to_client>')
def transfer_call(from_client, to_client):
    incoming_sid = client_to_incoming_sid[from_client]
    # client_to_incoming_sid[to_client] = incoming_sid
    trc = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    call = trc.calls.get(incoming_sid)
    to_client_url = url_for('incoming_voice_url', client_name=to_client)
    call.route(url=to_client_url, method='GET')

    return 'ok'


@app.route("/incoming_voice_url/<client_name>")
def incoming_voice_url(client_name):
    # call sid from twilio
    call_sid = request.args.get('CallSid')

    # construct the twiml response
    resp = twilio.twiml.Response()
    dial = resp.dial()
    dial.client(client_name)

    # store the mapping
    client_to_incoming_sid[client_name] = call_sid

    # dump the twiml
    return str(resp)


@app.route("/client/<client_name>")
def start(client_name):
    twilio_capability = TwilioCapability(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    twilio_capability.allow_client_incoming(client_name)

    capability_token = twilio_capability.generate()

    return render_template('client.html', capability_token=capability_token, client_name=client_name)

if __name__ == "__main__":
    app.run(debug=True)
