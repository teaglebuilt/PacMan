import pytest
from app.models import Service, Result
from tests import conftest



def test_service(db):
    service = Service(
        url='https://petstore.swagger.io/v2/swagger.json'
    )
    assert (service.url == "https://petstore.swagger.io/v2/swagger.json")
    assert (str(service) == "Service: https://petstore.swagger.io/v2/swagger.json")


def test_result(db):
    result = Result(
        url="https://petstore.swagger.io/v2/1",
        total_time=2.1969270360000053,
        result_all={
            "average": 0.21176482297999855,
            "fastest": 0.15303821700001663,
            "objects": [
                    {
                        "request_time": 0.2728469770000004,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.27592899600000464,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.27988752400000294,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.2897847929999955,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.2828241179999793,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.2860235250000187,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.2971986350000009,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.2973876669999811,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.30264269700001023,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.30598412200001235,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.1927728610000088,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.17836942100001352,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.20548504100000287,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.18109934799997518,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.19066294400002448,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.1883737440000175,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.19171147700001256,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.19789754399999993,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.20608038299999976,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.20281267999999386,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.18327905599997507,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.15666687999998885,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.1963894140000093,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.15683196999998472,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.1611597579999966,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.1784173839999994,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.16803106399999024,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.16265186199998993,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.17793394199998147,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.19036268700000392,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.18458852300000217,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.15303821700001663,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.16555019499998025,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.1910482380000076,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.16378821199998583,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.1701189360000228,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.19470285299999546,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.1734383849999972,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.1794625750000023,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.19182267799999408,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.2724262860000124,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.24654801299999463,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.25091385300001434,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.2771250469999984,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.28081444099998976,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.2955835059999856,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.28875013399999716,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.29346598899999776,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.28464471399999525,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.2912149409999927,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.22768730199999254,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.22899234999999862,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.22490044400001352,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.21257220900000107,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.19385015000000294,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.20299506599999972,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.2067704190000086,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.2110852059999786,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.20783770000002733,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.2280234739999969,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.18582399600001054,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.1792760539999847,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.18040377599999147,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.15549839400000565,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.19964629400001854,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.16900560900000983,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.17355048400000328,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.17942397499999174,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.1973443499999803,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.1852603239999837,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.1796170410000002,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.18260973799999647,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.18545053700000835,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.19398860100000093,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.17390715600001272,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.19024695599998154,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.18022517899999002,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.1806553190000102,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.19362473099999988,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.21459014200002002,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.17965405800001122,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.16460209899997835,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.18257508099998176,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.17415676599998164,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.17963810599999874,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.21100781600000573,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.16672642499997892,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.1849480229999756,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.1733956979999789,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.19977354200000264,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.24816000399999893,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.24070200500000283,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.23099439599999982,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.2468697809999867,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.2428214809999929,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.22844836599998075,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.24108629200000564,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.2456167260000086,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.25350367999999435,
                        "status_code": 404
                    },
                    {
                        "request_time": 0.250394727000014,
                        "status_code": 404
                    }
                ],
            "requests_per_min": 2731,
            "requests_per_sec": 46,
            "slowest": 0.30598412200001235,
            "total_time": 2.1969270360000053
        }
    )
    assert result.url == "https://petstore.swagger.io/v2/1"