package proxy

import java.lang.reflect.Proxy

inline fun <reified T : TestApiCall> createApi() = Proxy.newProxyInstance(
    ClassLoader.getSystemClassLoader(),
    arrayOf(TestApiCall::class.java)
) { _, method, _ ->

    val annotation = method.getAnnotation(Test::class.java)

    //api 요청
    println("${BuildConfig.currentPhase().prefix}${annotation.data}")

    //받아온 결과를 통해 데이터 맵핑 (여기서는 실제 api콜을 하지 않기때문에 임의로 작성)
    if (annotation.data.contains("kakao")) {
        Response("kakao", "카카오", "라이언")
    } else {
        Response("google", "구글코리아", "로버트 마틴")
    }
} as T