
class JSONRequestTestFixtureUtilities(object):

    @staticmethod
    def get_post_data(load_id=0, x=0, y=0):
        return {'loadId': load_id,
                'x': x,
                'y': y}

    @staticmethod
    def get_post_data_override_names(load_id_name='loadId',
                                     x_coordinate_name='x',
                                     y_coordinate_name='y'):
        return {load_id_name: 0,
                x_coordinate_name: 0,
                y_coordinate_name: 0}


class JSONRobotDatabaseDataTextFixtureUtilities(object):

    @staticmethod
    def get_robot_database_data(robot_id=0, battery_level=100, x=0, y=0):
        return {'robotId': robot_id,
                'batteryLevel': battery_level,
                'x': x,
                'y': y}

    @staticmethod
    def get_robot_database_data_override_names(robot_id_name='robotId',
                                               battery_level_name='batteryLevel',
                                               x_name='x',
                                               y_name='y'):
        return {robot_id_name: 0,
                battery_level_name: 100,
                x_name: 0,
                y_name: 0}
