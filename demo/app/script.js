function getMapData(mapSet) {
    var result = {};
    var key_set = mapSet.keySet();
    var it = key_set.iterator();
    while (it.hasNext()) {
        var key_str = it.next().toString();
        result[key_str] = mapSet.get(key_str).toString();
    }

    return result
}


function getXSign(params) {
    var result = '';
    Java.perform(function () {
        Java.enumerateClassLoaders({
            onMatch: function (loader) {
                try {
                    if (loader.findClass('com.taobao.wireless.security.adapter.JNICLibrary')) {
                        console.log('loader: ', loader);
                        Java.classFactory.loader = loader;
                    }
                } catch (error) {
                }
            },
            onComplete: function () {
            }
        });

        var JNICLibrary = Java.use('com.taobao.wireless.security.adapter.JNICLibrary');
        var hashMap = Java.use('java.util.HashMap');

        var a1 = Java.use('java.lang.Integer').$new(0);
        var p1 = Java.array('Ljava.lang.Object;', [a1]);
        var res1 = JNICLibrary.doCommandNative(22301, p1);
        console.log('res1: ', res1);

        var a2 = Java.use('java.lang.Integer').$new(0);
        var a3 = Java.use('java.lang.Boolean').$new(true);
        var p2 = Java.array('Ljava.lang.Object;', [a2, a3]);
        var res2 = JNICLibrary.doCommandNative(22302, p2);
        console.log('res2: ', res2);

        var a = '' +
            'YNCoyETQXFUDAD6xvGW8c/tk&&&' +
            '23181017&' +
            '7e5fa4a04006ccd2dd430485bf947743&' +
            '1624375174&' +
            'mtop.alibaba.mum.citem.get&' +
            '1.0&&' +
            '231200@tmall_android_10.7.0&' +
            'Av7FBE_0MsxQF2sMj7Ir0W182Q_p3_mlWCKy-pK45lTs&&&' +
            'openappkey=DEFAULT_AUTH&27&&&&&&&';

        var ps = [
            Java.use('java.lang.String').$new('23181017'),
            Java.use('java.lang.String').$new('YNCoyETQXFUDAD6xvGW8c/tk&&&23181017&7e5fa4a04006ccd2dd430485bf947743&1624375174&mtop.alibaba.mum.citem.get&1.0&&231200@tmall_android_10.7.0&Av7FBE_0MsxQF2sMj7Ir0W182Q_p3_mlWCKy-pK45lTs&&&openappkey=DEFAULT_AUTH&27&&&&&&&'),
            Java.use('java.lang.Boolean').$new(false),
            Java.use('java.lang.Integer').$new(0),
            Java.use('java.lang.String').$new('mtop.alibaba.mum.citem.get'),
            Java.use('java.lang.String').$new('pageId=&pageName='),
            null,
            null,
            null,
            Java.use('java.lang.String').$new('r_18'),
        ];
        var p3 = Java.array('Ljava.lang.Object;', ps);
        result = JNICLibrary.doCommandNative(70102, p3);
        result = getMapData(Java.cast(result, hashMap));
    });

    return result;
}


// 8.11.0
function getXSign8110(signData) {
    var result = ''
    Java.perform(function () {
        Java.enumerateClassLoaders({
            onMatch: function (loader) {
                try {
                    if (loader.findClass('com.taobao.wireless.security.adapter.JNICLibrary')) {
                        Java.classFactory.loader = loader;
                    }
                } catch (error) {
                }
            }, onComplete: function () {
            }
        });

        var hashMap = Java.use('java.util.HashMap').$new();
        var JNICLibrary = Java.use('com.taobao.wireless.security.adapter.JNICLibrary');
        hashMap.put('INPUT', signData['input'])

        var params = [
            hashMap,
            Java.use('java.lang.String').$new(signData['app_key']),
            Java.use('java.lang.Integer').$new(7),
            Java.use('java.lang.String').$new(''),
            Java.use('java.lang.Boolean').$new(true),
        ];

        var ps = Java.array('Ljava.lang.Object;', params);
        result = JNICLibrary.doCommandNative(10401, ps).toString();
    })
    return result
}

// 8.11.0
function getMiniWua8110(wuaData) {
    var result = ''
    Java.perform(function () {
        Java.enumerateClassLoaders({
            onMatch: function (loader) {
                try {
                    if (loader.findClass('com.taobao.wireless.security.adapter.JNICLibrary')) {
                        Java.classFactory.loader = loader;
                    }
                } catch (error) {
                }
            }, onComplete: function () {
            }
        });

        var JNICLibrary = Java.use('com.taobao.wireless.security.adapter.JNICLibrary');

        var params = [
            Java.use('java.lang.String').$new(wuaData['time_str']),
            Java.use('java.lang.String').$new(wuaData['app_key']),
            Java.use('java.lang.Integer').$new(8),
            Java.use('java.lang.String').$new(''),
            Java.use('java.lang.String').$new(wuaData['input']),
            Java.use('java.lang.Integer').$new(0),
        ];
        var ps = Java.array('Ljava.lang.Object;', params);
        result = JNICLibrary.doCommandNative(20102, ps).toString();
    })

    return result
}


rpc.exports = {
    getxsign: getXSign,
    getxsign8110: getXSign8110,
    getminiwua8110: getMiniWua8110
};
