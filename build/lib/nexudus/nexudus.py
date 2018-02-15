"""
API Implementation to connect to Nexudus Application.
"""

import json

import requests
from requests.auth import HTTPBasicAuth

DOMAIN_URL = 'https://spaces.nexudus.com/api'


class MissingRequiredArgumentException(Exception):
    def __init__(self, message):
        super(MissingRequiredArgumentException, self).__init__(message)


def parse_params(local_arg_dict):
    params = {}
    for attr, value in local_arg_dict.items():
        if attr == 'self':
            continue
        if value is not None:
            params[attr] = value
    return params


def parse_body(local_arg_dict):
    payload = {}
    for attr, value in local_arg_dict.items():
        if attr == 'self':
            continue
        if value is not None:
            payload[attr] = value
        else:
            raise MissingRequiredArgumentException(
                "%s arg is required." % attr)
    return payload


class Nexudus(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.session = self.create_session()

    def create_session(self):
        session = requests.Session()
        session.auth = HTTPBasicAuth(self.username, self.password)
        return session


class AccessToken(Nexudus):
    BASE_URL = DOMAIN_URL + '/spaces/accesstokens'

    def get_access_tokens(self,
                          AccessToken_Id=None,
                          AccessToken_Business=None,
                          AccessToken_AccessCode=None,
                          AccessToken_Description=None,
                          AccessToken_MinutesIncluded=None,
                          AccessToken_MacAddress=None,
                          AccessToken_MinutesLeft=None,
                          AccessToken_LastAccess=None):
        """
        API to get all access tokens.
        """
        params = parse_params(locals())
        return self.session.get(self.BASE_URL, params=params)

    def get_access_token_by_id(self, AccessToken_Id):
        """
        API to get access token by access token id.
        """
        return self.session.get(self.BASE_URL + '/{}'.format(AccessToken_Id))

    def create_access_token(self,
                            BusinessId=None,
                            AccessCode=None,
                            MinutesIncluded=None,
                            MinutesLeft=None):
        """
        API to create an access token.
        All params are required.
        """
        payload = parse_body(locals())
        return self.session.post(self.BASE_URL, data=payload)

    def delete_access_token(self, AccessToken_Id):
        """
        API to delete access token by access token id.
        """
        return self.session.delete(
            self.BASE_URL + '/{}'.format(AccessToken_Id))

    def update_access_token(self,
                            Id=None,
                            BusinessId=None,
                            AccessCode=None,
                            MinutesIncluded=None,
                            MinutesLeft=None):
        """
        API to update an access token.
        All params are required.
        """
        payload = parse_body(locals())
        return self.session.put(self.BASE_URL, data=payload)


class Booking(Nexudus):
    BASE_URL = DOMAIN_URL + '/spaces/bookings'

    def get_bookings(self,
                     Booking_Id=None,
                     Booking_Resource=None,
                     Booking_Coworker=None,
                     Booking_ExtraService=None,
                     Booking_FromTime=None,
                     Booking_ToTime=None,
                     Booking_Notes=None,
                     Booking_InternalNotes=None,
                     Booking_ChargeNow=None,
                     Booking_InvoiceNow=None,
                     Booking_DoNotUseBookingCredit=None,
                     Booking_PurchaseOrder=None,
                     Booking_DiscountCode=None,
                     Booking_LastNotificationTime=None,
                     Booking_GoogleCalendarId=None,
                     Booking_GoogleEventId=None,
                     Booking_Tentative=None,
                     Booking_Online=None,
                     Booking_TeamsAtTheTimeOfBooking=None,
                     Booking_TariffAtTheTimeOfBooking=None,
                     Booking_RepeatSeriesUniqueId=None,
                     Booking_RepeatBooking=None,
                     Booking_Repeats=None,
                     Booking_WhichBookingsToUpdate=None,
                     Booking_RepeatEvery=None,
                     Booking_RepeatUntil=None,
                     Booking_RepeatOnMondays=None,
                     Booking_RepeatOnTuesdays=None,
                     Booking_RepeatOnWednesdays=None,
                     Booking_RepeatOnThursdays=None,
                     Booking_RepeatOnFridays=None,
                     Booking_RepeatOnSaturdays=None,
                     Booking_RepeatOnSundays=None,
                     Booking_Reminded=None,
                     Booking_MrmReminded=None,
                     Booking_Invoiced=None,
                     Booking_InvoiceDate=None,
                     Booking_KisiKeyId=None,
                     Booking_StartScheduledJobId=None,
                     Booking_EndScheduledJobId=None,
                     Booking_Billed=None,
                     Booking_FromTimeLocal=None,
                     Booking_ToTimeLocal=None,
                     Booking_InvoiceDateLocal=None,
                     Booking_Resource_Name=None,
                     Booking_Coworker_FullName=None,
                     Booking_ExtraService_Name=None):
        """
        API to get all bookings.
        """
        params = parse_params(locals())
        return self.session.get(self.BASE_URL, params=params)

    def get_booking_by_id(self, Booking_Id):
        """
        API to get booking by booking id.
        """
        return self.session.get(self.BASE_URL + '/{}'.format(Booking_Id))

    def create_booking(self, ResourceId=None, FromTime=None, ToTime=None):
        """
        API to create a booking.
        All params are required.
        """
        payload = parse_body(locals())
        return self.session.post(self.BASE_URL, data=payload)

    def delete_booking(self, Booking_Id):
        """
        API to delete booking by booking id.
        """
        return self.session.delete(self.BASE_URL + '/{}'.format(Booking_Id))

    def update_booking(self,
                       Id=None,
                       ResourceId=None,
                       FromTime=None,
                       ToTime=None):
        """
        API to update a booking.
        All params are required.
        """
        payload = parse_body(locals())
        return self.session.put(self.BASE_URL, data=payload)


class BookingProduct(Nexudus):
    BASE_URL = DOMAIN_URL + '/spaces/bookingproducts'

    def get_booking_products(self,
                             BookingProduct_Id=None,
                             BookingProduct_Booking=None,
                             BookingProduct_Product=None,
                             BookingProduct_InvoiceInMinutes=None,
                             BookingProduct_Quantity=None,
                             BookingProduct_Product_Name=None):
        """
        API to get all booking products.
        """
        params = parse_params(locals())
        return self.session.get(self.BASE_URL, params=params)

    def get_booking_product_by_id(self, BookingProduct_Id):
        """
        API to get booking product by booking product id.
        """
        return self.session.get(
            self.BASE_URL + '/{}'.format(BookingProduct_Id))

    def create_booking_product(self,
                               BookingId=None,
                               ProductId=None,
                               Quantity=None):
        """
        API to create a booking product.
        All params are required.
        """
        payload = parse_body(locals())
        return self.session.post(self.BASE_URL, data=payload)

    def delete_booking_product(self, BookingProduct_Id):
        """
        API to delete booking product by booking product id.
        """
        return self.session.delete(
            self.BASE_URL + '/{}'.format(BookingProduct_Id))

    def update_booking_product(self,
                               Id=None,
                               BookingId=None,
                               ProductId=None,
                               Quantity=None):
        """
        API to update a booking.
        All params are required.
        """
        payload = parse_body(locals())
        return self.session.put(self.BASE_URL, data=payload)
