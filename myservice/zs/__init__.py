from os.path import dirname, abspath
import zserio

schema_entry_point = dirname(abspath(__file__))+"/myservice/myservice.zs"
zserio.generate(schema_entry_point, "zs_api")