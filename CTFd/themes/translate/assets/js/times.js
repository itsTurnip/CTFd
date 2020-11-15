import Moment from "moment";
import $ from "jquery";

export default () => {
  $("[data-time]").each((i, elem) => {
    elem.innerText = Moment($(elem).data("time"))
      .local()
      .format("DD MMMM, hh:mm:ss");
  });
};
