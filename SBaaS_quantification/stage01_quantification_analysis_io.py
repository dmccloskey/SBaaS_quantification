from .stage01_quantification_analysis_query import stage01_quantification_analysis_query
from SBaaS_base.sbaas_template_io import sbaas_template_io
# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData

class stage01_quantification_analysis_io(stage01_quantification_analysis_query,
                                    sbaas_template_io #abstract io methods
                                    ):
    pass  