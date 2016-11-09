var siteApp = angular.module("siteApp",[]);

$(function() {setInterval(function() {
  $("#bodyer").css("height", "auto");
  var vh = $(window).height();
  var hh = $("header").height();
  var bh = $("#bodyer").height();
  var fh = $("footer").height();
  if (vh > hh + bh + fh) $("#bodyer").height(vh - hh - fh);
}, 200);});

function upload_file(opts) {
  o = opts.ofile||"";
  $("#file_iframe").remove();
  var iframe = $("<iframe id='file_iframe' style='display:none;'></iframe>");
  $("body").append(iframe);
  var body = $(iframe[0].contentWindow.document.body);
  var form = $("<form action='/upload_file' method='post' enctype='multipart/form-data'></form>");
  var ofile = $("<input type='hidden' name='ofile' value='" + o + "'>");
  var nfile = $("<input type='file' name='nfile'/>");
  body.append(form.append(ofile).append(nfile));
  iframe[0].onload = function() {
    var result = $(iframe[0].contentWindow.document.body).html();
    if(opts.onComplete) opts.onComplete($.parseJSON(result));
  };
  nfile.click();
  nfile.change(function() {
    form.submit();
  });
}

siteApp.controller("MemberCtrl", ["$scope", "$http", function($scope, $http){
  $scope.filter = {
    rows: 10,
    page: 0
  };
  $scope.list = [];
  $("#datetimepicker").datetimepicker({
    format: "yyyy-mm-dd",
    startView: 4,
    minView: 2,
    autoclose: true,
    language: "zh-CN"
  });
  $scope.gender_str = function(val){
    return val == "M" ? "男" : "女";
  };
  $scope.avatar_str = function(url) {
    if(url == "")
      return "/assets/images/avatar.default.jpg";
    return url;
  };
  $scope.create_edit = function() {
    $scope.member = {
      id: "",
      phone: "",
      email: "",
      name: "",
      gender: "M",
      dob: "1985-01-01",
      avatar: "",
      signature: "",
      description: "",
      status: 0
    };
    $("#editor").modal("show");
  };
  $scope.submit = function(evt) {
    $(evt.target).button("loading");
    $http.post("update_member", $scope.member).success(function(e) {
      $(evt.target).button("reset");
      $("#editor").modal("hide");
    });
  };
  $scope.select_avatar = function() {
    upload_file({
      ofile: $scope.member.avatar,
      onComplete: function(e) {
        if(e.status == 0) $scope.$apply(function(){ $scope.member.avatar = e.url; });
        console.log($scope.member);
      }
    });
  };
  function fetch(page) {
    $scope.page = page;
    $http.get("fetch_members", $scope.filter).success(function(e){
      if(e.status == 0) {
        $scope.list = e.data;
        $("#member-pager").twbsPagination({
          totalPages: e.count,
          startPage: page + 1,
          visiblePages: 10,
          first: "首页",
          prev: "上一页",
          next: "下一页",
          last: "未页",
          onPageClick: function(event, index) {
            fetch(index - 1);
          }
        });
      }
    });
  }
  fetch(0);
}]);