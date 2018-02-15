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
        API to update a booking product.
        All params are required.
        """
        payload = parse_body(locals())
        return self.session.put(self.BASE_URL, data=payload)


class CheckIn(Nexudus):
    BASE_URL = DOMAIN_URL + '/spaces/checkins'

    def get_checkins(self,
                     Checkin_Id=None,
                     Checkin_Coworker=None,
                     Checkin_Business=None,
                     Checkin_FromTime=None,
                     Checkin_ToTime=None,
                     Checkin_CountsTowardsPlanLimits=None,
                     Checkin_CoworkerTimePassGuid=None,
                     Checkin_AutoCheckout=None,
                     Checkin_LastActivity=None,
                     Checkin_MacAddresses=None,
                     Checkin_TeamsAtTheTimeOfCheckin=None,
                     Checkin_TariffAtTheTimeOfCheckin=None,
                     Checkin_Coworker_FullName=None,
                     Checkin_Business_Name=None):
        """
        API to get all checkins.
        """
        params = parse_params(locals())
        return self.session.get(self.BASE_URL, params=params)

    def get_checkin_by_id(self, Checkin_Id):
        """
        API to get checkin by checkin id.
        """
        return self.session.get(self.BASE_URL + '/{}'.format(Checkin_Id))

    def create_checkin(self, BusinessId=None, FromTime=None):
        """
        API to create a checkin.
        All params are required.
        """
        payload = parse_body(locals())
        return self.session.post(self.BASE_URL, data=payload)

    def delete_checkin(self, Checkin_Id):
        """
        API to delete checkin by checkin id.
        """
        return self.session.delete(self.BASE_URL + '/{}'.format(Checkin_Id))

    def update_checkin(self, Id=None, BusinessId=None, FromTime=None):
        """
        API to update a checkin.
        All params are required.
        """
        payload = parse_body(locals())
        return self.session.put(self.BASE_URL, data=payload)


class Coworker(Nexudus):
    BASE_URL = DOMAIN_URL + '/spaces/coworkers'

    def get_checkins(self,
                     Coworker_Id=None,
                     Coworker_Tariff=None,
                     Coworker_NextTariff=None,
                     Coworker_FullName=None,
                     Coworker_Salutation=None,
                     Coworker_Gender=None,
                     Coworker_Email=None,
                     Coworker_CreateUser=None,
                     Coworker_Address=None,
                     Coworker_PostCode=None,
                     Coworker_CityName=None,
                     Coworker_State=None,
                     Coworker_Country=None,
                     Coworker_SimpleTimeZone=None,
                     Coworker_MobilePhone=None,
                     Coworker_LandLine=None,
                     Coworker_DateOfBirth=None,
                     Coworker_NickName=None,
                     Coworker_BusinessArea=None,
                     Coworker_CompanyName=None,
                     Coworker_ProfileWebsite=None,
                     Coworker_ProfileTags=None,
                     Coworker_ProfileSummary=None,
                     Coworker_Twitter=None,
                     Coworker_Facebook=None,
                     Coworker_Linkedin=None,
                     Coworker_Skype=None,
                     Coworker_ProfileIsPublic=None,
                     Coworker_InvoicingBusiness=None,
                     Coworker_BillingEmail=None,
                     Coworker_BillingName=None,
                     Coworker_BillingAddress=None,
                     Coworker_BillingPostCode=None,
                     Coworker_BillingCityName=None,
                     Coworker_BillingState=None,
                     Coworker_BillingCountry=None,
                     Coworker_BillingSimpleTimeZone=None,
                     Coworker_TaxRate=None,
                     Coworker_TaxIDNumber=None,
                     Coworker_BankName=None,
                     Coworker_BankAccount=None,
                     Coworker_NotifyOnNewInvoice=None,
                     Coworker_EnableGoCardlessPayments=None,
                     Coworker_GoCardlessContractNumber=None,
                     Coworker_LastOverDueInvoiceReminder=None,
                     Coworker_LastLowCreditReminder=None,
                     Coworker_RegularPaymentProvider=None,
                     Coworker_RegularPaymentContractNumber=None,
                     Coworker_CardNumber=None,
                     Coworker_DoNotProcessInvoicesAutomatically=None,
                     Coworker_AllowNetworkCheckin=None,
                     Coworker_CheckinSinceLastRenewal=None,
                     Coworker_MinutesSinceLastRenewal=None,
                     Coworker_AccessCardId=None,
                     Coworker_EzeepUserId=None,
                     Coworker_EzeepFreePrinting=None,
                     Coworker_PaperCutPayAsYouPrint=None,
                     Coworker_PaperCutFreePrinting=None,
                     Coworker_Tag=None,
                     Coworker_Notes=None,
                     Coworker_User=None,
                     Coworker_Active=None,
                     Coworker_BillingDay=None,
                     Coworker_NextInvoice=None,
                     Coworker_IncludeSignupFee=None,
                     Coworker_ApplyProRating=None,
                     Coworker_NextAutoInvoice=None,
                     Coworker_RegistrationDate=None,
                     Coworker_CancellationDate=None,
                     Coworker_GeneralTermsAccepted=None,
                     Coworker_PricePlanTermsAccepted=None,
                     Coworker_LastRenewal=None,
                     Coworker_LastInvoiceAttempt=None,
                     Coworker_Custom1=None,
                     Coworker_Custom2=None,
                     Coworker_Custom3=None,
                     Coworker_Custom4=None,
                     Coworker_Custom5=None,
                     Coworker_Custom6=None,
                     Coworker_Custom7=None,
                     Coworker_Custom8=None,
                     Coworker_Custom9=None,
                     Coworker_Custom10=None,
                     Coworker_Custom11=None,
                     Coworker_Custom12=None,
                     Coworker_Custom13=None,
                     Coworker_Custom14=None,
                     Coworker_Custom15=None,
                     Coworker_Custom16=None,
                     Coworker_Custom17=None,
                     Coworker_Custom18=None,
                     Coworker_Custom19=None,
                     Coworker_Custom20=None,
                     Coworker_Custom21=None,
                     Coworker_Custom22=None,
                     Coworker_Custom23=None,
                     Coworker_Custom24=None,
                     Coworker_Custom25=None,
                     Coworker_Custom26=None,
                     Coworker_Custom27=None,
                     Coworker_Custom28=None,
                     Coworker_Custom29=None,
                     Coworker_Custom30=None,
                     Coworker_Tariff_Name=None,
                     Coworker_Businesses=None,
                     Coworker_Teams=None):
        """
        API to get all coworkers.
        """
        params = parse_params(locals())
        return self.session.get(self.BASE_URL, params=params)

    def get_coworker_by_id(self, Coworker_Id):
        """
        API to get coworker by coworker id.
        """
        return self.session.get(self.BASE_URL + '/{}'.format(Coworker_Id))

    def create_coworker(self,
                        FullName=None,
                        Email=None,
                        CountryId=None,
                        SimpleTimeZoneId=None,
                        CheckinSinceLastRenewal=None,
                        MinutesSinceLastRenewal=None,
                        BillingDay=None,
                        AddedBusinesses=[],
                        AddedTeams=[]):
        """
        API to create a coworker.
        All params are required.
        """
        payload = parse_body(locals())
        return self.session.post(self.BASE_URL, data=payload)

    def delete_coworker(self, Coworker_Id):
        """
        API to delete coworker by coworker id.
        """
        return self.session.delete(self.BASE_URL + '/{}'.format(Coworker_Id))

    def update_coworker(self,
                        Id=None,
                        FullName=None,
                        Email=None,
                        CountryId=None,
                        SimpleTimeZoneId=None,
                        CheckinSinceLastRenewal=None,
                        MinutesSinceLastRenewal=None,
                        BillingDay=None,
                        AddedBusinesses=[],
                        AddedTeams=[]):
        """
        API to update a coworker.
        All params are required.
        """
        payload = parse_body(locals())
        return self.session.put(self.BASE_URL, data=payload)


class PricePlanHistory(Nexudus):
    BASE_URL = DOMAIN_URL + '/spaces/coworkerpriceplanhistories'

    def get_price_plan_histories(
            self,
            CoworkerPricePlanHistory_Id=None,
            CoworkerPricePlanHistory_Coworker=None,
            CoworkerPricePlanHistory_OldTariffName=None,
            CoworkerPricePlanHistory_NewTariffName=None,
            CoworkerPricePlanHistory_OldTariffUniqueId=None,
            CoworkerPricePlanHistory_NewTariffUniqueId=None,
            CoworkerPricePlanHistory_IsUpgrade=None,
            CoworkerPricePlanHistory_Notes=None,
            CoworkerPricePlanHistory_OldValue=None,
            CoworkerPricePlanHistory_NewValue=None,
            CoworkerPricePlanHistory_OldQuantity=None,
            CoworkerPricePlanHistory_NewQuantity=None,
            CoworkerPricePlanHistory_CreatedOnLocal=None):
        """
        API to get all price_plan_histories.
        """
        params = parse_params(locals())
        return self.session.get(self.BASE_URL, params=params)

    def get_price_plan_history_by_id(self, CoworkerPricePlanHistory_Id):
        """
        API to get price_plan_history by price_plan_history id.
        """
        return self.session.get(
            self.BASE_URL + '/{}'.format(CoworkerPricePlanHistory_Id))


class Resource(Nexudus):
    BASE_URL = DOMAIN_URL + '/spaces/resources'

    def get_resources(self,
                      Resource_Id=None,
                      Resource_Business=None,
                      Resource_Name=None,
                      Resource_ResourceType=None,
                      Resource_Description=None,
                      Resource_Visible=None,
                      Resource_DisplayOrder=None,
                      Resource_GroupName=None,
                      Resource_Projector=None,
                      Resource_Internet=None,
                      Resource_ConferencePhone=None,
                      Resource_StandardPhone=None,
                      Resource_WhiteBoard=None,
                      Resource_LargeDisplay=None,
                      Resource_Catering=None,
                      Resource_TeaAndCoffee=None,
                      Resource_Drinks=None,
                      Resource_SecurityLock=None,
                      Resource_CCTV=None,
                      Resource_VoiceRecorder=None,
                      Resource_AirConditioning=None,
                      Resource_Heating=None,
                      Resource_NaturalLight=None,
                      Resource_AllowMultipleBookings=None,
                      Resource_Allocation=None,
                      Resource_BookInAdvanceLimit=None,
                      Resource_LateBookingLimit=None,
                      Resource_LateCancellationLimit=None,
                      Resource_IntervalLimit=None,
                      Resource_NoReturnPolicy=None,
                      Resource_NoReturnPolicyAllResources=None,
                      Resource_NoReturnPolicyAllUsers=None,
                      Resource_MaxBookingLength=None,
                      Resource_MinBookingLength=None,
                      Resource_Shifts=None,
                      Resource_GoogleCalendarId=None,
                      Resource_KisiGroupId=None,
                      Resource_AccessControlGroupId=None,
                      Resource_Longitude=None,
                      Resource_Latitude=None,
                      Resource_ResourceType_Name=None,
                      Resource_Tariffs=None,
                      Resource_LinkedResources=None):
        """
        API to get all resources.
        """
        params = parse_params(locals())
        return self.session.get(self.BASE_URL, params=params)

    def get_resource_by_id(self, Resource_Id):
        """
        API to get resource by resource id.
        """
        return self.session.get(self.BASE_URL + '/{}'.format(Resource_Id))

    def create_resource(self,
                        BusinessId=None,
                        Name=None,
                        ResourceTypeId=None,
                        DisplayOrder=None,
                        AddedTariffs=[],
                        AddedLinkedResources=[]):
        """
        API to create a resource.
        All params are required.
        """
        payload = parse_body(locals())
        return self.session.post(self.BASE_URL, data=payload)

    def delete_resource(self, Resource_Id):
        """
        API to delete resource by resource id.
        """
        return self.session.delete(self.BASE_URL + '/{}'.format(Resource_Id))

    def update_resource(self,
                        Id=None,
                        BusinessId=None,
                        Name=None,
                        ResourceTypeId=None,
                        DisplayOrder=None,
                        AddedTariffs=[],
                        AddedLinkedResources=[]):
        """
        API to update a resource.
        All params are required.
        """
        payload = parse_body(locals())
        return self.session.put(self.BASE_URL, data=payload)


class ResourceTimeSlot(Nexudus):
    BASE_URL = DOMAIN_URL + '/spaces/resourcetimeslots'

    def get_resource_time_slots(self,
                                ResourceTimeSlot_Id=None,
                                ResourceTimeSlot_Resource=None,
                                ResourceTimeSlot_FromTime=None,
                                ResourceTimeSlot_ToTime=None,
                                ResourceTimeSlot_DayOfWeek=None):
        """
        API to get all resource_time_slots.
        """
        params = parse_params(locals())
        return self.session.get(self.BASE_URL, params=params)

    def get_resource_time_slot_by_id(self, ResourceTimeSlot_Id):
        """
        API to get resource_time_slot by resource_time_slot id.
        """
        return self.session.get(
            self.BASE_URL + '/{}'.format(ResourceTimeSlot_Id))

    def create_resource_time_slot(self,
                                  ResourceId=None,
                                  FromTime=None,
                                  ToTime=None):
        """
        API to create a resource_time_slot.
        All params are required.
        """
        payload = parse_body(locals())
        return self.session.post(self.BASE_URL, data=payload)

    def delete_resource_time_slot(self, ResourceTimeSlot_Id):
        """
        API to delete resource_time_slot by resource_time_slot id.
        """
        return self.session.delete(
            self.BASE_URL + '/{}'.format(ResourceTimeSlot_Id))

    def update_resource_time_slot(self,
                                  Id=None,
                                  ResourceId=None,
                                  FromTime=None,
                                  ToTime=None):
        """
        API to update a resource_time_slot.
        All params are required.
        """
        payload = parse_body(locals())
        return self.session.put(self.BASE_URL, data=payload)