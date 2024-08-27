from setuptools import setup

setup(name='OpenSeesAPI',
      version='0.15.0',
      description='A OpenSees Wrapper in Python',
      url='http://github.com/nassermarafi/OpenSeesAPI',
      author='Nasser Marafi',
      author_email='marafi@uw.edu',
      license='MIT',
      packages=['OpenSeesAPI',
                    'OpenSeesAPI.Analysis',
                    'OpenSeesAPI.Model',
                        'OpenSeesAPI.Model.Element',
                            'OpenSeesAPI.Model.Element.Material',
                    'OpenSeesAPI.Helpers',
                'test'],
      zip_safe=False)
