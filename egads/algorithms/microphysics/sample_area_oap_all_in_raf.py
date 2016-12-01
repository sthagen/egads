__author__ = "mfreer"
__date__ = "$Date:: 2013-02-17 18:01#$"
__version__ = "$Revision:: 163       $"
__all__ = ['SampleAreaOapAllInRaf']

import egads.core.egads_core as egads_core
import egads.core.metadata as egads_metadata
import numpy

class SampleAreaOapAllInRaf(egads_core.EgadsAlgorithm):
    """

    FILE        sample_area_oap_all_in_raf.py

    VERSION     $Revision: 163 $

    CATEGORY    Microphysics

    PURPOSE     Calculation of 'all-in' sample area size for OAP probes

    DESCRIPTION Calculation of 'all-in' sample area size for OAP probes such as
                the 2DP, CIP, etc. The sample area varies by the number of shadowed
                diodes. This routine calculates a sample area per bin.

    INPUT       Lambda      coeff.          nm      Laser wavelength
                D_arms      coeff.          mm      Distance between probe arms
                dD          coeff.          um      Diode diameter
                M           coeff.          _       Probe magnification factor
                N           coeff.          _       Number of diodes in array

    OUTPUT      SA          Vector[bins]    m2      Sample area

    SOURCE      NCAR-RAF

    REFERENCES  NCAR-RAF Bulletin No. 24

    """


    def __init__(self, return_Egads=True):
        egads_core.EgadsAlgorithm.__init__(self, return_Egads)

        self.output_metadata = egads_metadata.VariableMetadata({'units':'m^2',
                                                               'long_name':'sample area, all in',
                                                               'standard_name':'',
                                                               'Category':['PMS Probe']})

        self.metadata = egads_metadata.AlgorithmMetadata({'Inputs':['Lambda', 'D_arms', 'dD', 'M', 'N'],
                                                          'InputUnits':['nm', 'mm', 'um', '', ''],
                                                          'InputTypes':['coeff','coeff','coeff','coeff','coeff','coeff'],
                                                          'InputDescription':['Laser wavelength','Distance between probe arms','Diode diameter','Probe magnification factor','Number of diodes in array'],
                                                          'Outputs':['SA'],
                                                          'OutputDescription':['Sample area'],
                                                          'Purpose':'Calculation of "all-in" sample area size for OAP probes',
                                                          'Description':'Calculation of "all-in" sample area size for OAP probes such as the 2DP, CIP, etc. The sample area varies by the number of shadowed diodes. This routine calculates a sample area per bin.',
                                                          'Processor':self.name,
                                                          'ProcessorDate':__date__,
                                                          'ProcessorVersion':__version__,
                                                          'DateProcessed':self.now()},
                                                          self.output_metadata)




    def run(self, Lambda, D_arms, dD, M, N):

        return egads_core.EgadsAlgorithm.run(self, Lambda, D_arms, dD, M, N)

    def _algorithm(self, Lambda, D_arms, dD, M, N):

        SA = numpy.array([])
        Lambda_mm = Lambda * 1e-6  # convert wavelength to mm
        dD_mm = dD * 1e-3  # convert diameter to mm

        for i in range(N):
            X = i + 1
            R = X * dD_mm / 2.0
            DOF = 6 * R ** 2 / (Lambda_mm)
            if DOF > D_arms:
                DOF = D_arms

            ESW = dD_mm * (N - X - 1) / M

            SA = numpy.append(SA, DOF * ESW * 1e-6)  # convert mm2 to m2

        return SA
