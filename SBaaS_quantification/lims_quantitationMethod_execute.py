
from .lims_quantitationMethod_io import lims_quantitationMethod_io
from .lims_quantitationMethod_dependencies import lims_quantitationMethod_dependencies
#resources
#TODO:
from rpy2.robjects.packages import importr
import rpy2.robjects as robjects

class lims_quantitationMethod_execute(lims_quantitationMethod_io,
                                      lims_quantitationMethod_dependencies
                                    ):

    def execute_quantitationMethodUpdate(self, quant_method_ids_I = []):
        '''calculate regression parameters for all components
        that have not been determined'''

        if quant_method_ids_I:
            quant_method_ids = quant_method_ids_I;
        else:
            quant_method_ids = [];
            quant_method_ids = self.get_quantMethodIds();
        for id in quant_method_ids:
            # get the samples and components that make were used to make
            # the quantitation method
            print(id);
            calibrator_samples = None;
            component_names = [];
            calibrator_samples,component_names = self.get_quantSamplesAndComponents(id);
            for n in component_names:
                print(n);
                # get the quant method parameters for each component
                fit,weighting,use_area = self.get_quantMethodParameters(id,n);
                # get the quant method info
                actual_concentration,ratio,dilution_factor=self.get_quantMethodInfo(calibrator_samples,use_area,n);
                # calculate the quant regression parameters for each component
                slope,intercept,correlation,lloq,uloq,points = self.calculate_regressionParameters(fit,weighting,actual_concentration,ratio,dilution_factor);
                # update the quantitation_method table
                self.update_quantitationMethod(id,n,slope,intercept,correlation,lloq,uloq,points);

    def execute_quantitationMethodComparison(self):
        '''Query and write calibration regression parameters to file'''

        # get the components that are in all of the calibration methods
        component_names = [];
        component_names = self.get_allComponents();
        # get all the quantitation method IDs
        quant_method_ids = [];
        quant_method_ids = self.get_allQuantMethodIds();
        with open('quantitationMethodComparison.csv', 'w') as csvfile:
            # write header to file
            csv_writer = csv.writer(csvfile)
            header = [];
            columns = [];
            column_names = ['slope','intercept','correlation','lloq','uloq','points'];
            for c in column_names:
                for i in quant_method_ids:
                    header.append(i);
                    columns.append(c);
            header.insert(0,'');
            columns.insert(0,'Component_Name');
            csv_writer.writerow(header);
            csv_writer.writerow(columns);
            # loop through each component
            for n in component_names:
                slopes = [];
                intercepts = [];
                correlations = [];
                lloqs = [];
                uloqs = [];
                points = [];
                for id in quant_method_ids:
                    # query regression parameters
                    slope = 0;
                    intercept = 0;
                    correlation = 0;
                    lloq = 0;
                    uloq = 0;
                    point = 0;
                    slope,intercept,correlation,lloq,uloq,point = self.get_quantMethodRegression(id,n);
                    slopes.append(slope);
                    intercepts.append(intercept);
                    correlations.append(correlation);
                    lloqs.append(lloq);
                    uloqs.append(uloq);
                    points.append(point);

                # write row to file
                row = [n];
                row.extend(slopes);
                row.extend(intercepts);
                row.extend(correlations);
                row.extend(lloqs);
                row.extend(uloqs);
                row.extend(points);
                csv_writer.writerow(row);