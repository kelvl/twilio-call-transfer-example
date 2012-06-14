Twilio Call Transfer Example
=========
Contrived but short example on how to create series of browser softphones using Twilio, Twilio Client's APIs and transfer incoming PSTN calls between them.

***

####Requirements
 - [Flask](http://flask.pocoo.org/docs/)
 - [Twilio Python library](https://github.com/twilio/twilio-python)
 - [A public facing host](http://aws.amazon.com)

#### Documentation 

This project exposes 3 different endpoints

##### /client/&lt;client_name&gt;

Displays a page with a Twilio Client under the client name: &lt;client_name&gt;

Calls directed to the client named, &lt;client_name&gt; will ring the browser showing this page. 

The following TwiML calls the Twilio Client on [/client/alice](/client/alice)

    <Response>
        <Dial>
            <Client>alice</Client>
        </Dial>
    </Response>

##### /incoming_voice_url/&lt;client_name&gt;

Used as the Voice URL for your Twilio Number to forward all calls made to that number to the designated &lt;client_name&gt;

##### /transfer_call/&lt;from_client&gt;/to/&lt;to_client&gt;

Called within a Javascript AJAX call to transfer the current call from &lt;from_client&gt; to &lt;to_client&gt;

*** 

#### Installation

1. Clone the repository
2. Edit TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN
3. Added http://&lt;server&gt;/incoming_voice_url/alice as your phone number's Voice URL in the Twilio Dashboard
4. Open 2 browser windows to http://&lt;server&gt;/client/alice and http://&lt;server&gt;/client/bob
5. Call in to your Twilio number and Alice's browser phone will ring and click on the transfer to Bob button.

