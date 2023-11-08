# coding: utf-8

"""
    Weather API

    # Introduction WeatherAPI.com provides access to weather and geo data via a JSON/XML restful API. It allows developers to create desktop, web and mobile applications using this data very easy. We provide following data through our API:     - Real-time weather - 14 day weather forecast - Historical Weather - Marine Weather and Tide Data - Future Weather (Upto 365 days ahead) - Daily and hourly intervals - 15 min interval (Enterprise only) - Astronomy - Time zone - Location data - Sports - Search or Autocomplete API - Weather Alerts - Air Quality Data - Bulk Request  # Getting Started    You need to [signup](https://www.weatherapi.com/signup.aspx) and then you can find your API key under [your account](https://www.weatherapi.com/login.aspx), and start using API right away!  Try our weather API by using interactive [API Explorer](https://www.weatherapi.com/api-explorer.aspx).  We also have SDK for popular framework/languages available on [Github](https://github.com/weatherapicom/) for quick integrations.  If you find any features missing or have any suggestions, please [contact us](https://www.weatherapi.com/contact.aspx).    # Authentication    API access to the data is protected by an API key. If at anytime, you find the API key has become vulnerable, please regenerate the key using Regenerate button next to the API key.    Authentication to the WeatherAPI.com API is provided by passing your API key as request parameter through an API .      ##  key parameter  key=YOUR API KEY    # noqa: E501

    OpenAPI spec version: 1.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class ForecastAstro(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'sunrise': 'str',
        'sunset': 'str',
        'moonrise': 'str',
        'moonset': 'str',
        'moon_phase': 'str',
        'moon_illumination': 'str'
    }

    attribute_map = {
        'sunrise': 'sunrise',
        'sunset': 'sunset',
        'moonrise': 'moonrise',
        'moonset': 'moonset',
        'moon_phase': 'moon_phase',
        'moon_illumination': 'moon_illumination'
    }

    def __init__(self, sunrise=None, sunset=None, moonrise=None, moonset=None, moon_phase=None, moon_illumination=None, _configuration=None):  # noqa: E501
        """ForecastAstro - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._sunrise = None
        self._sunset = None
        self._moonrise = None
        self._moonset = None
        self._moon_phase = None
        self._moon_illumination = None
        self.discriminator = None

        if sunrise is not None:
            self.sunrise = sunrise
        if sunset is not None:
            self.sunset = sunset
        if moonrise is not None:
            self.moonrise = moonrise
        if moonset is not None:
            self.moonset = moonset
        if moon_phase is not None:
            self.moon_phase = moon_phase
        if moon_illumination is not None:
            self.moon_illumination = moon_illumination

    @property
    def sunrise(self):
        """Gets the sunrise of this ForecastAstro.  # noqa: E501


        :return: The sunrise of this ForecastAstro.  # noqa: E501
        :rtype: str
        """
        return self._sunrise

    @sunrise.setter
    def sunrise(self, sunrise):
        """Sets the sunrise of this ForecastAstro.


        :param sunrise: The sunrise of this ForecastAstro.  # noqa: E501
        :type: str
        """

        self._sunrise = sunrise

    @property
    def sunset(self):
        """Gets the sunset of this ForecastAstro.  # noqa: E501


        :return: The sunset of this ForecastAstro.  # noqa: E501
        :rtype: str
        """
        return self._sunset

    @sunset.setter
    def sunset(self, sunset):
        """Sets the sunset of this ForecastAstro.


        :param sunset: The sunset of this ForecastAstro.  # noqa: E501
        :type: str
        """

        self._sunset = sunset

    @property
    def moonrise(self):
        """Gets the moonrise of this ForecastAstro.  # noqa: E501


        :return: The moonrise of this ForecastAstro.  # noqa: E501
        :rtype: str
        """
        return self._moonrise

    @moonrise.setter
    def moonrise(self, moonrise):
        """Sets the moonrise of this ForecastAstro.


        :param moonrise: The moonrise of this ForecastAstro.  # noqa: E501
        :type: str
        """

        self._moonrise = moonrise

    @property
    def moonset(self):
        """Gets the moonset of this ForecastAstro.  # noqa: E501


        :return: The moonset of this ForecastAstro.  # noqa: E501
        :rtype: str
        """
        return self._moonset

    @moonset.setter
    def moonset(self, moonset):
        """Sets the moonset of this ForecastAstro.


        :param moonset: The moonset of this ForecastAstro.  # noqa: E501
        :type: str
        """

        self._moonset = moonset

    @property
    def moon_phase(self):
        """Gets the moon_phase of this ForecastAstro.  # noqa: E501


        :return: The moon_phase of this ForecastAstro.  # noqa: E501
        :rtype: str
        """
        return self._moon_phase

    @moon_phase.setter
    def moon_phase(self, moon_phase):
        """Sets the moon_phase of this ForecastAstro.


        :param moon_phase: The moon_phase of this ForecastAstro.  # noqa: E501
        :type: str
        """

        self._moon_phase = moon_phase

    @property
    def moon_illumination(self):
        """Gets the moon_illumination of this ForecastAstro.  # noqa: E501


        :return: The moon_illumination of this ForecastAstro.  # noqa: E501
        :rtype: str
        """
        return self._moon_illumination

    @moon_illumination.setter
    def moon_illumination(self, moon_illumination):
        """Sets the moon_illumination of this ForecastAstro.


        :param moon_illumination: The moon_illumination of this ForecastAstro.  # noqa: E501
        :type: str
        """

        self._moon_illumination = moon_illumination

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ForecastAstro, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ForecastAstro):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ForecastAstro):
            return True

        return self.to_dict() != other.to_dict()
