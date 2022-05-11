function DemaciaClient(wsURL) {
    this.wsURL = wsURL;
    this.handlers = {};
    this.socket = {};
    this.base64 = false;
    if (!wsURL) {
        throw new Error('wsURL can not be empty!!')
    }
    this.webSocketFactory = this.resolveWebSocketFactory();
    this.connect()
}

DemaciaClient.prototype.resolveWebSocketFactory = function () {
    if (typeof window === 'object') {
        var theWebSocket = window.WebSocket ? window.WebSocket : window.MozWebSocket;
        return function (wsURL) {

            function WindowWebSocketWrapper(wsURL) {
                this.mSocket = new theWebSocket(wsURL);
            }

            WindowWebSocketWrapper.prototype.close = function () {
                this.mSocket.close();
            };

            WindowWebSocketWrapper.prototype.onmessage = function (onMessageFunction) {
                this.mSocket.onmessage = onMessageFunction;
            };

            WindowWebSocketWrapper.prototype.onopen = function (onOpenFunction) {
                this.mSocket.onopen = onOpenFunction;
            };
            WindowWebSocketWrapper.prototype.onclose = function (onCloseFunction) {
                this.mSocket.onclose = onCloseFunction;
            };

            WindowWebSocketWrapper.prototype.send = function (message) {
                this.mSocket.send(message);
            };

            return new WindowWebSocketWrapper(wsURL);
        }
    }
    if (typeof WebSocket === 'object') {
        return function (wsURL) {
            return new theWebSocket(wsURL);
        }
    }
    throw new Error('当前 js 环境不支持 websocket');
};

DemaciaClient.prototype.connect = function () {
    console.log('connect to wsURL: ', this.wsURL);
    var _this = this;
    try {
        this.socket = this.webSocketFactory(this.wsURL);
    } catch (e) {
        console.log('create connection failed,reconnect after 2s');
        setTimeout(function () {
            _this.connect()
        }, 2000)
    }

    this.socket.onmessage(function (event) {
        _this.handleRequest(event.data)
    });

    this.socket.onopen(function (event) {
        console.log('open a demacia client connection')
    });

    this.socket.onclose(function (event) {
        console.log('disconnected ,reconnection after 2s');
        setTimeout(function () {
            _this.connect()
        }, 2000)
    });
};

DemaciaClient.prototype.handleRequest = function (requestJson) {
    console.log('handleRequest: ', requestJson);
    var request = JSON.parse(requestJson);

    if (!request['action_name']) {
        this.sendMessage(request, '需要请求参数 action_name', -1);
        return
    }

    var action = request['action_name'];
    if (!this.handlers[action]) {
        this.sendMessage(request, `${action} 没有 handler 操作程序`, -1);
        return
    }

    var theHandler = this.handlers[action];
    var _this = this;
    try {
        theHandler(request, function (response) {
            try {
                _this.sendMessage(request, response, 0)
            } catch (e) {
                _this.sendMessage(request, `${e}`, -1);
            }
        }, function (errorMessage) {
            _this.sendMessage(request, `${errorMessage}`, -1)
        })
    } catch (e) {
        console.log("error: ", e);
        _this.sendMessage(request, `${e}`, -1);
    }
};

DemaciaClient.prototype.sendMessage = function (request, response, status) {
    var responseJson = {
        data: response,
        status: status,
        group_id: request.group_id,
        action_name: request.action_name,
        __process_id__: request.__process_id__,
    };

    var responseText = JSON.stringify(responseJson);
    console.log('sendMessage.response: ', responseText);

    this.socket.send(responseText);
};

DemaciaClient.prototype.registerAction = function (action, handler) {
    if (typeof action !== 'string') {
        throw new Error('action 必须是字符串');
    }
    if (typeof handler !== 'function') {
        throw new Error('handler 必须是函数');
    }
    console.log('register action: ', action);
    this.handlers[action] = handler;
    return this;
};


