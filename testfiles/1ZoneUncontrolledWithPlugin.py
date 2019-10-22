from pyenergyplus.plugin import EnergyPlusPlugin


class MyPlugin(EnergyPlusPlugin):

    def main(self):
        db_handle = self.transfer.get_variable_handle(u"SITE OUTDOOR AIR DRYBULB TEMPERATURE", u"ENVIRONMENT")
        my_glycol = self.functional.glycol("water")
        outdoor_db = self.transfer.get_variable_value(db_handle)
        water_cp_at_outdoor_db = my_glycol.specific_heat(outdoor_db)
        print("Inside Plugin; Outdoor DB = %f, Water CP @ ODB = %f" % (outdoor_db, water_cp_at_outdoor_db))
        return 0


# class MyFasterPlugin(EnergyPlusPlugin):
#
#     def __init__(self):
#         super().__init__()
#         self.init_once = True
#         self.db_handle = 0
#         self.my_glycol = None
#
#     def main(self):
#         if self.init_once:
#            self.db_handle = self.transfer.get_variable_handle(u"SITE OUTDOOR AIR DRYBULB TEMPERATURE", u"ENVIRONMENT")
#            self.my_glycol = self.functional.glycol("water")
#         outdoor_db = self.transfer.get_variable_value(self.db_handle)
#         water_cp_at_outdoor_db = self.my_glycol.specific_heat(outdoor_db)
#         print("Inside Plugin; Outdoor DB = %f, Water CP @ ODB = %f" % (outdoor_db, water_cp_at_outdoor_db))
#         return 0
