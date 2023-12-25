# pylint: disable=too-few-public-methods, missing-module-docstring, broad-exception-caught,invalid-name

from enum import Enum
from typing import Optional, List, Dict, Any, Union
from dataclasses import dataclass, field
from .version import VERSION


# pylint: disable=too-many-instance-attributes
@dataclass
class RenderParams:
    """
    Parameters for video rendering.
    """
    data: Optional[List] = None
    bucket_name: Optional[str] = None
    region: Optional[str] = None
    out_name: Optional[str] = None
    composition: str = ""
    serve_url: str = ""
    frames_per_lambda: Optional[int] = None
    input_props: Optional[Dict] = None
    codec: str = 'h264'
    version: str = ""
    image_format: str = 'jpeg'
    crf: Optional[int] = None
    env_variables: Optional[Dict] = None
    max_retries: int = 1
    jpeg_quality: int = 80
    privacy: str = 'public'
    color_space: str = 'default'
    log_level: str = 'info'
    frame_range: Optional[str] = None
    timeout_in_milliseconds: Optional[int] = 30000
    chromium_options: Optional[Dict] = None
    scale: Optional[int] = 1
    every_nth_frame: Optional[int] = 1
    number_of_gif_loops: Optional[int] = 0
    concurrency_per_lambda: Optional[int] = 1
    download_behavior: Dict = field(default_factory=lambda: {
                                    'type': 'play-in-browser'})
    muted: bool = False
    overwrite: bool = False
    audio_bitrate: Optional[int] = None
    video_bitrate: Optional[int] = None
    webhook: Optional[str] = None
    force_height: Optional[int] = None
    offthreadvideo_cache_size_in_bytes: Optional[int] = None
    force_width: Optional[int] = None
    audio_codec: Optional[str] = None
    renderer_function_name: Optional[str] = None
    pro_res_profile: Optional[str] = None
    x264_preset: Optional[str] = None
    pixel_format: Optional[str] = None
    delete_after: Optional[str] = None

    def serialize_params(self) -> Dict:
        """
        Convert instance attributes to a dictionary for serialization.
        """
        parameters = {
            'rendererFunctionName': self.renderer_function_name,
            'framesPerLambda': self.frames_per_lambda,
            'composition': self.composition,
            'serveUrl': self.serve_url,
            'inputProps': self.input_props,
            'codec': self.codec,
            'imageFormat': self.image_format,
            'maxRetries': self.max_retries,
            'jpegQuality': self.jpeg_quality,
            'envVariables': self.env_variables,
            'privacy': self.privacy,
            'colorSpace': self.color_space,
            'logLevel': self.log_level,
            'frameRange': self.frame_range,
            'outName': self.out_name,
            'timeoutInMilliseconds': self.timeout_in_milliseconds,
            'chromiumOptions': self.chromium_options if self.chromium_options is not None else {},
            'scale': self.scale,
            'everyNthFrame': self.every_nth_frame,
            'numberOfGifLoops': self.number_of_gif_loops,
            'concurrencyPerLambda': self.concurrency_per_lambda,
            'downloadBehavior': self.download_behavior,
            'muted': self.muted,
            'version': VERSION,
            'overwrite': self.overwrite,
            'audioBitrate': self.audio_bitrate,
            'videoBitrate': self.video_bitrate,
            'webhook': self.webhook,
            'forceHeight': self.force_height,
            'offthreadVideoCacheSizeInBytes': self.offthreadvideo_cache_size_in_bytes,
            'forceWidth': self.force_width,
            'bucketName': self.bucket_name,
            'audioCodec': self.audio_codec,
            'x264Preset': self.x264_preset,
            'deleteAfter': self.delete_after,
            'type': 'start'
        }

        if self.crf is not None:
            parameters['crf'] = self.crf

        if self.env_variables is None:
            parameters['envVariables'] = {}

        if self.pixel_format is not None:
            parameters['pixelFormat'] = self.pixel_format

        if self.pro_res_profile is not None:
            parameters['proResProfile'] = self.pro_res_profile

        if self.x264_preset is not None:
            parameters['x264Preset'] = self.x264_preset

        return parameters


# pylint: disable=too-many-instance-attributes
class RenderResponse:
    """
    Response data after rendering.
    """

    def __init__(self, bucketName, renderId):
        self.bucketName = bucketName
        self.renderId = renderId


@dataclass
class RenderProgressParams:
    """
    Parameters for checking the progress of video rendering.
    """

    render_id: str
    bucket_name: str
    function_name: str
    region: str

    def serialize_params(self) -> Dict:
        """
        Convert instance attributes to a dictionary for serialization.
        """
        parameters = {
            'renderId': self.render_id,
            'bucketName': self.bucket_name,
            'type': 'status',
            "version": VERSION,
            "s3OutputProvider": None,
        }
        return parameters


@dataclass
class CostsInfo:
    """
    Represents the cost-related information for a specific service or product.

    Attributes:
        accrued_so_far (float): The total cost that has been accrued so far.
        display_cost (str): The cost displayed to the user, possibly formatted as a string.
        currency (str): The type of currency used for the costs, e.g., 'USD', 'EUR'.
        disclaimer (str): Any disclaimer or additional information related to the costs.
    """
    accrued_so_far: float
    display_cost: str
    currency: str
    disclaimer: str


@dataclass
class RenderStillOnLambdaOutput:
    """
    Represents the output information of a rendering operation performed on AWS Lambda.

    Attributes:
        estimated_price (CostsInfo): 
            An object containing detailed cost information related to the rendering.
        url (str): The URL where the rendered image is stored or can be accessed.
        size_in_bytes (int): The size of the rendered image file in bytes.
        bucket_name (str): The name of the S3 bucket where the rendered image is stored.
        render_id (str): A unique identifier for the rendering operation.
        cloud_watch_logs (str): The CloudWatch logs associated with the rendering operation.
    """
    estimated_price: CostsInfo
    url: str
    size_in_bytes: int
    bucket_name: str
    render_id: str
    cloud_watch_logs: str


class ValidStillImageFormats(Enum):
    """
    Enumeration of valid image formats for still images.

    Attributes:
        PNG: Represents the PNG image format.
        JPEG: Represents the JPEG image format.
        PDF: Represents the PDF format for images.
        WEBP: Represents the WEBP image format.
    """
    PNG = 'png'
    JPEG = 'jpeg'
    PDF = 'pdf'
    WEBP = 'webp'


class Privacy(Enum):
    """
    Enumeration of privacy settings.

    Attributes:
        PUBLIC: Indicates a public setting.
        PRIVATE: Indicates a private setting.
    """
    PUBLIC = 'public'
    PRIVATE = 'private'


class LogLevel(Enum):
    """
    Enumeration for different levels of logging.

    Attributes:
        VERBOSE: Verbose logging level.
        INFO: Informational logging level.
        WARN: Warning logging level.
        ERROR: Error logging level.
    """
    VERBOSE = 'verbose'
    INFO = 'info'
    WARN = 'warn'
    ERROR = 'error'


class OpenGlRenderer(Enum):
    """
    Enumeration of OpenGL renderer options.

    Attributes:
        SWANGLE: Represents the SWANGLE OpenGL renderer.
        ANGLE: Represents the ANGLE OpenGL renderer.
        EGL: Represents the EGL OpenGL renderer.
        SWIFTSHADER: Represents the SWIFTSHADER OpenGL renderer.
        VULKAN: Represents the VULKAN OpenGL renderer.
    """
    SWANGLE = 'swangle'
    ANGLE = 'angle'
    EGL = 'egl'
    SWIFTSHADER = 'swiftshader'
    VULKAN = 'vulkan'


@dataclass
class ChromiumOptions:
    """
    Options for configuring the Chromium browser.

    Attributes:
        ignore_certificate_errors (Optional[bool]): If True, ignores certificate errors.
        disable_web_security (Optional[bool]): If True, disables web security.
        gl (Optional[OpenGlRenderer]): Specifies the OpenGL renderer to use.
        headless (Optional[bool]): If True, runs Chromium in headless mode.
        user_agent (Optional[str]): Specifies a custom user agent.
        enable_multi_process_on_linux (Optional[bool]): 
            If True, enables multi-process mode on Linux.
    """
    ignore_certificate_errors: Optional[bool] = None
    disable_web_security: Optional[bool] = None
    gl: Optional[OpenGlRenderer] = None
    headless: Optional[bool] = None
    user_agent: Optional[str] = None
    enable_multi_process_on_linux: Optional[bool] = None


@dataclass
class CustomCredentialsWithoutSensitiveData:
    """
    Represents credentials without sensitive data.

    Attributes:
        endpoint (str): The endpoint associated with the credentials.
    """
    endpoint: str


@dataclass
class CustomCredentials(CustomCredentialsWithoutSensitiveData):
    """
    Represents custom credentials, extending credentials without sensitive data.

    Attributes:
        access_key_id (Optional[str]): The access key ID.
        secret_access_key (Optional[str]): The secret access key.
    """
    access_key_id: Optional[str] = None
    secret_access_key: Optional[str] = None


@dataclass
class OutNameInputObject:
    """
    Defines output naming and storage options.

    Attributes:
        bucket_name (str): The name of the S3 bucket for output storage.
        key (str): The key name within the S3 bucket.
        s3_output_provider (Optional[CustomCredentials]):
             Optional custom credentials for the S3 output provider.
    """
    bucket_name: str
    key: str
    s3_output_provider: Optional[CustomCredentials] = None


@dataclass
class PlayInBrowser:
    """
    Represents the behavior to play content directly in the browser.

    Attributes:
        type (str): The type of in-browser action (e.g., 'play-in-browser').
    """
    type: str


@dataclass
class Download:
    """
    Represents the behavior to download content.

    Attributes:
        type (str): The type of download action.
        file_name (Optional[str]): The name of the file to be downloaded, if specified.
    """
    type: str
    file_name: Optional[str]


class DeleteAfter(Enum):
    """
    Enumeration for specifying the time period after which an item should be deleted.

    Attributes:
        ONE_DAY: Represents deletion after one day.
        THREE_DAYS: Represents deletion after three days.
        SEVEN_DAYS: Represents deletion after seven days.
        THIRTY_DAYS: Represents deletion after thirty days.
    """
    ONE_DAY = '1-day'
    THREE_DAYS = '3-days'
    SEVEN_DAYS = '7-days'
    THIRTY_DAYS = '30-days'


@dataclass
class BaseRenderParams:
    region: str
    function_name: str
    serve_url: str


@dataclass
class RenderStillParams:
    """
    Parameters for video rendering.
    """
    composition: str
    data: Optional[List] = None
    input_props: Optional[Dict[str, Any]] = None
    image_format: ValidStillImageFormats = ValidStillImageFormats.JPEG
    privacy: Privacy = Privacy.PUBLIC
    max_retries: Optional[int] = None
    env_variables: Optional[Dict[str, str]] = None
    jpeg_quality: Optional[int] = None
    frame: Optional[int] = None
    log_level: Optional[LogLevel] = None
    out_name: Optional[Union[str, OutNameInputObject]] = None
    timeout_in_milliseconds: Optional[int] = None
    chromium_options: Optional[ChromiumOptions] = None
    scale: Optional[float] = None
    download_behavior: Dict = field(default_factory=lambda: {
                                    'type': 'play-in-browser'})
    force_width: Optional[int] = None
    force_height: Optional[int] = None
    force_bucket_name: Optional[str] = None
    dump_browser_logs: Optional[bool] = None
    delete_after: Optional[DeleteAfter] = None

    def serialize_params(self) -> Dict:
        """
            Serializes the parameters of the current object into a dictionary.

            This method consolidates both mandatory and optional attributes of the object 
            into a single dictionary. Mandatory attributes include region, functionName, 
            serveUrl, composition, inputProps, imageFormat, and privacy. Optional attributes 
            are added to the dictionary only if they are not None.

            The optional attributes include maxRetries, envVariables, jpegQuality, frame, 
            logLevel, outName, timeoutInMilliseconds, chromiumOptions, scale, downloadBehavior, 
            forceWidth, forceHeight, forceBucketName, dumpBrowserLogs, and deleteAfter. 
            Default values are provided for 'inputProps' (empty dictionary) and 'downloadBehavior' 
            ('type': 'play-in-browser') if they are not explicitly set.

            Returns:
                Dict: A dictionary containing all the serialized parameters of the object.
        """
        parameters = {

            'composition': self.composition,
            'inputProps': self.input_props or {},  # Provide a default empty dict if None
            'imageFormat': self.image_format,
            'privacy': self.privacy,
            'type': 'start'
        }
        optional_fields = {
            'maxRetries': self.max_retries,
            'envVariables': self.env_variables,
            'jpegQuality': self.jpeg_quality,
            'frame': self.frame,
            'logLevel': self.log_level,
            'outName': self.out_name,
            'timeoutInMilliseconds': self.timeout_in_milliseconds,
            'chromiumOptions': self.chromium_options,
            'scale': self.scale,
            'downloadBehavior': self.download_behavior or {'type': 'play-in-browser'},
            'forceWidth': self.force_width,
            'forceHeight': self.force_height,
            'forceBucketName': self.force_bucket_name,
            'dumpBrowserLogs': self.dump_browser_logs,
            'deleteAfter': self.delete_after,
        }

        # Add optional fields only if they are not None
        for key, value in optional_fields.items():
            if value is not None:
                parameters[key] = value

        return parameters


class RenderProgress:
    """
    Progress of video rendering.
    """

    def __init__(self):
        self.overallProgress = float()
        self.chunks = int()
        self.done = bool()
        self.encodingStatus = None
        self.costs = None
        self.renderId = str()
        self.renderMetadata = None
        self.outputFile = None
        self.outKey = None
        self.timeToFinish = None
        self.errors = []
        self.fatalErrorEncountered = bool()
        self.currentTime = int()
        self.renderSize = int()
        self.outputSizeInBytes = None
        self.lambdasInvoked = int()
        self.framesRendered = None
