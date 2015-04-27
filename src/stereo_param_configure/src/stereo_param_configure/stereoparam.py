"""
File: stereoparam.py
Author: Yifei Zhang
Email: njzhangyifei@gmail.com
Github: https://github.com/njzhangyifei
Description:
    Function for ROS node stereo_param_configure
"""

class StereoParam(object):
    """StereoParamConfigure
    @type  self._client: dynamic_reconfigure.client.Client
    """

    def __init__(self, client):
        """
        @type client: dynamic_reconfigure.client.Client
        """
        self._client = client

    def set_exposure_time(self, time):
        """set the exposure time for ueye node
        :time: The desired exposure time
        """
        if not isinstance(time, float):
            if isinstance(time, int):
                time = float(time)
            else:
                return
        assert isinstance(time, float)
        param_dict = {"exposure_time" : time}
        self._client.update_configuration(param_dict)

    def set_auto_exposure(self, auto_exposure):
        """set the auto exposure
        :auto_exposure: whether to use auto exposure
        """
        if not isinstance(auto_exposure, bool):
            return
        param_dict = {"auto_exposure" : auto_exposure}
        self._client.update_configuration(param_dict)

    def set_gain(self, gain):
        """set gain
        :gain : the gain value
        """
        if not isinstance(gain, int):
            return
        param_dict = {"gain" : gain}
        self._client.update_configuration(param_dict)

    def set_auto_gain(self, auto_gain):
        """set the auto gain
        :auto_gain : whether to use auto gain
        """
        if not isinstance(auto_gain, bool):
            return
        param_dict = {"auto_gain" : auto_gain}
        self._client.update_configuration(param_dict)

    def set_frame_rate(self, frame_rate):
        """set frame rate
        :frame_rate : frame rate
        """
        if not isinstance(frame_rate, float):
            return
        """
        :TODO
        """
        return
