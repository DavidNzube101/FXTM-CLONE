from flask import Blueprint, render_template, flash, request, redirect, url_for, current_app, send_from_directory, session, jsonify
from werkzeug.utils import secure_filename
from flask_login import login_required, current_user


import base64
import imghdr
import random
from datetime import datetime, timedelta
import datetime as dt

from . import DateToolKit as dtk
from .db import db
from .db import dbORM
from . import encrypt
from . import ScreenGoRoute
from . import function_pool
from . import id_generator

routeHandler = Blueprint('routeHandler', __name__)
rh = routeHandler

@rh.route("/")
def renderLandingPage():

	return render_template("landing.html", DeviceType=function_pool.detectDeviceType(request), status=())

@rh.route("/dashboard")
def viewDashboard():
	u = dbORM.get_all("UserFXTM")[f'{current_user.id}']

	return ScreenGoRoute.go_to("1", redirect=True, request=request)

@rh.route("/deposit-funds")
def depositFunds():

	return ScreenGoRoute.go_to("DepositFunds.html", _redirect=False, request=request)

@rh.route("/withdraw-funds")
def withdrawFunds():

	return ScreenGoRoute.go_to("WithdrawFunds.html", _redirect=False, request=request)

@rh.route("/my-fxtm-wallet")
def fxtmWallets():

	return ScreenGoRoute.go_to("FXTMWallets.html", _redirect=False, request=request)

@rh.route("/transaction-history")
def transactionHistory():

	return ScreenGoRoute.go_to("TransactionHistory.html", _redirect=False, request=request)

@rh.route("/internal-transfers")
def internalTranfers():

	return ScreenGoRoute.go_to("InternalTransfers.html", _redirect=False, request=request)

@rh.route("/my-trading-accounts")
def tradingAccount():

	return ScreenGoRoute.go_to("TradingAccount.html", _redirect=False, request=request)

@rh.route('/demo-account')
def demoAccount():

	return ScreenGoRoute.go_to("DemoAccount.html", _redirect=False, request=request)

@rh.route('/complete-registration')
def completeRegistration():

	return ScreenGoRoute.go_to("CompleteRegistration.html", _redirect=False, request=request)

@rh.route("/upload-document/<string:what_doc>")
def UplaodDoc(what_doc):
	doc_def = {
		"bvn": 1,
		"nid": 2,
		"pp": 3,
		"utb": 4
	}
	u = dbORM.get_all("UserFXTM")[f'{current_user.id}']
	vef_docs = eval(u['verify_docs'])

	for doc_x, doc_y in doc_def.items():
		# if what_doc == doc_y
		print(doc_y, what_doc)
		if what_doc == doc_x:
			vef_docs.append(doc_y)
			dbORM.update_entry(
		        "UserFXTM", 
		        f"{dbORM.find_one('UserFXTM', 'id', current_user.id)}", 
		        encrypt.encrypter(str(
		            {
		                "verify_docs": f"{vef_docs}"
		            }
		        )), 
		        dnd=False
		    )

	return redirect(url_for("routeHandler.completeRegistration"))