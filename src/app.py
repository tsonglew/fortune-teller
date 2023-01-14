from typing import Union

from api.beans.divination import Divination
from api.beans.double_divination import DoubleDivination
from common.utils.chrono import ChronoUtil
from common.utils.divination import DivinationUtil
from common.utils.double_divination import DoubleDivinationUtil
from common.utils.luck import LuckUtil
from common.utils.mutal_divination import MutualDivinationUtil
from flask import Flask, jsonify, request
from service.divination import DivinationService
from service.double_divination import DoubleDivinationService
from service.runner import RunnerService

app = Flask(__name__)

chrono_util = ChronoUtil("../assets/chrono.json")
divination_util = DivinationUtil("../assets/divination.json")
double_divination_util = DoubleDivinationUtil(
    "../assets/double_divination.json",
    "../assets/double_divination_property_name.txt",
    divination_util,
)
mutual_divination_util = MutualDivinationUtil(
    "../assets/mutual_divination.txt", double_divination_util
)
luck_util = LuckUtil(double_divination_util)

divination_service = DivinationService(divination_util)
double_divination_service = DoubleDivinationService(double_divination_util)
runner_service = RunnerService(
    divination_util,
    double_divination_util,
    chrono_util,
    mutual_divination_util,
    luck_util,
)


@app.route("/")
def index():
    return "Hello World"


@app.route("/doubleDivination/<arg>", methods=["GET"])
def double_divination(arg: Union[int, str]):
    return jsonify(
        (
            double_divination_util.get_double_divination_by_name(str(arg))
            or double_divination_util.get_double_divination_by_value(int(arg))
        ).to_json()
    )


@app.route("/divination/<arg>", methods=["GET"])
def divination(arg: Union[int, str]):
    return (
        divination_util.get_divination_by_name(str(arg))
        or divination_util.get_divination_by_value(int(arg))
    ).to_json()


@app.route("/doubleDivinationList", methods=["GET"])
def double_divination_list():
    return double_divination_service.get_divination_list()


@app.route("/divinationList", methods=["GET"])
def divination_list():
    return divination_service.get_divination_list()


@app.route("/run", methods=["GET"])
def run():
    # TODO: check inupt params
    nums = [int(i) for i in str(request.args.get("nums")).split(",")]
    nums.extend([0] * (2 - len(nums)))
    return runner_service.run(nums).to_json()
