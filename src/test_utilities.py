
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
