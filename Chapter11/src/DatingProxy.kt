import java.lang.reflect.InvocationHandler
import java.lang.reflect.InvocationTargetException
import java.lang.reflect.Method
import java.lang.reflect.Proxy

interface PersonBean {
    var name: String
    var gender: String
    var interests: String
    var hotOrNotRating: Int
}

class PersonBeanImpl : PersonBean {
    override var name: String = ""
    override var gender: String = ""
    override var interests = ""
    override var hotOrNotRating = 0
        set(rating) {
            field += rating
            ratingCount++
        }
        get() = if (ratingCount == 0) 0 else field / ratingCount

    var ratingCount = 0

    override fun toString(): String {
        return "$name, $gender $interests, $hotOrNotRating"
    }
}

class OwnerInvocationHandler(private val person: PersonBean) : InvocationHandler {
    @Throws(IllegalAccessException::class)
    override fun invoke(proxy: Any?, method: Method?, args: Array<out Any>?): Any {
        return try {
            when {
                method!!.name.startsWith("get") -> method.invoke(person, args!!)
                else -> throw IllegalAccessException()
            }
        } catch (e: InvocationTargetException) {
            e.printStackTrace()
        }
    }
}

class NotOwnerInvocationHandler(private val person: PersonBean) : InvocationHandler {
    @Throws(IllegalAccessException::class)
    override fun invoke(proxy: Any?, method: Method?, args: Array<out Any>?): Any {
        return try {
            return if (method!!.name == "setHorOrNotRating") method.invoke(person, args)
            else throw IllegalAccessException()
        } catch (e: InvocationTargetException) {
            e.printStackTrace()
        }
    }
}

fun getOwnerProxy(person: PersonBean): PersonBean {
    return Proxy.newProxyInstance(
        person.javaClass.classLoader,
        person.javaClass.interfaces,
        OwnerInvocationHandler(person)) as PersonBean
}

fun getNonOwnerProxy(person: PersonBean): PersonBean {
    return Proxy.newProxyInstance(
        person.javaClass.classLoader,
        person.javaClass.interfaces,
        NotOwnerInvocationHandler(person)) as PersonBean
}