var siteApp = angular.module("siteApp",[]);

$(function() {setInterval(function() {
  $("#bodyer").css("height", "auto");
  var vh = $(window).height();
  var hh = $("header").height();
  var bh = $("#bodyer").height();
  var fh = $("footer").height();
  if (vh > hh + bh + fh) $("#bodyer").height(vh - hh - fh);
}, 200);});

siteApp.controller("UserCtrl", ["$scope", "$http", function($scope, $http){
  $scope.filter = {
    rows: 10,
    page: 0
  };
  $scope.list = [];
  $http.get("fetch_users", $scope.filter).success(function(e){
    if(e.status == 0) {
      $scope.list = e.data;
    }
  });
}]);