        except:
17	            return False
18	
19	
20	class PIP(object):
21	    @classmethod
22	    def run(cls, command, check_output=False):
…	
26	        try:
27	            return PIP.run_python_m(*command.split(), check_output=check_output)
28	        except subprocess.CalledProcessError as e:
