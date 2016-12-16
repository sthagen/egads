#!/usr/bin/env python
"""EGADS: EUFAR General Airborne Data-processing Software

EGADS (EUFAR General Airborne Data-processing Software) is a Python-based
toolbox for processing airborne atmospheric data. EGADS provides a framework
for researchers to apply expert-contributed algorithms to data files, and acts
as a platform for data intercomparison. Algorithms used in EGADS were
contributed by members of the EUFAR Expert Working Groups and are mature and
well-established in the scientific community.
"""


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

classifiers = """\
Development Status :: 4 - Beta
Environment :: Console
Intended Audience :: Developers
Intended Audience :: Education
Intended Audience :: Science/Research
License :: OSI Approved :: BSD License
Natural Language :: English
Programming Language :: Python
Programming Language :: Python 2
Programming Language :: Python 2.7
Topic :: Scientific/Engineering :: Atmospheric Science
"""

doclines = __doc__.split('\n')

setup(name='egads',
      version='0.6.0',
      description=doclines[0],
      long_description='\n'.join(doclines[2:]),
      author='EUFAR',
      author_email='bureau@eufar.net',
      maintainer='Olivier Henry',
      maintainer_email='olivier.henry@meteo.fr',
      url='http://www.eufar.net',
      download_url='http://www.eufar.net/software-tools/tool/eufar-general-airborne-data-processing-software-core-da-cedg-osr',
      license='New BSD License',
      keywords=['airbornescience', 'netcdf', 'nasa-ames', 'eufar', 'science',
                  'microphysics', 'thermodynamics'],
      packages=['egads',
                  'egads.core',
                  'egads.algorithms',
		  'egads.algorithms.comparisons',
		  'egads.algorithms.corrections',
		  'egads.algorithms.mathematics',
                  'egads.algorithms.microphysics',
                  'egads.algorithms.radiation',
                  'egads.algorithms.thermodynamics',
                  'egads.algorithms.transforms',
                  'egads.input',
                  'egads.tests',
		  'egads.thirdparty.nappy',
		  'egads.thirdparty.nappy.config',
		  'egads.thirdparty.nappy.contrib',
		  'egads.thirdparty.nappy.na_error',
		  'egads.thirdparty.nappy.na_file',
		  'egads.thirdparty.nappy.nc_interface',
		  'egads.thirdparty.nappy.script',
		  'egads.thirdparty.nappy.utils',
		  'egads.thirdparty.pml_wq',
          'egads.thirdparty.pml_wq.iop_model',
          'egads.thirdparty.pml_wq.iop_model',
          'egads.thirdparty.pml_wq.iop_model.config',
          'egads.thirdparty.pml_wq.iop_model.data',
          'egads.thirdparty.pml_wq.test_data',
          'egads.thirdparty.quantities',
		  'egads.thirdparty.quantities.constants',
		  'egads.thirdparty.quantities.tests',
		  'egads.thirdparty.quantities.units'],
      package_data={
	      'egads.thirdparty.nappy': ['*.ini'],
          'egads.thirdparty.nappy.config':['*.ini']
	      },
      classifiers=filter(None, classifiers.split("\n")),
      requires=['numpy (>=1.10.1)', 'scipy (>=0.15.0)', 'netCDF4 (>=1.1.9)', 'python_dateutil (>=2.4.2)'],
      install_requires=['numpy >= 1.10.1', 'scipy >=0.15.0', 'netCDF4 >= 1.1.9', 'python_dateutil >= 2.4.2'],
      )
