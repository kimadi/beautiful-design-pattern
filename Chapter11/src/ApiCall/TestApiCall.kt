package proxy

@Target(AnnotationTarget.FUNCTION)
@Retention(AnnotationRetention.RUNTIME)
annotation class Test(val data: String)

interface TestApiCall {
    @Test("www.kakao.com")
    fun callKakao(): Response

    @Test("www.google.com")
    fun callGoogle(): Response
}

data class Response(val pageName: String, val text: String, val author: String)
