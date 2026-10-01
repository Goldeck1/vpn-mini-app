import { useState, useEffect } from 'react'
import './App.css'

const PLANS: SubscriptionPlan[] = [
  {
    id: '1_month',
    name: '1 месяц',
    duration: '30 дней',
    price: 299,
    originalPrice: 299,
    features: [
      '🚀 Высокая скорость',
      '🌍 Все сервера',
      '📱 5 устройств',
      '💬 Поддержка 24/7',
    ],
  },
  {
    id: '3_month',
    name: '3 месяца',
    duration: '90 дней',
    price: 699,
    originalPrice: 897,
    discount: 22,
    features: [
      '🚀 Высокая скорость',
      '🌍 Все сервера',
      '📱 5 устройств',
      '💬 Поддержка 24/7',
      '⭐ Выгоднее',
    ],
  },
  {
    id: '12_month',
    name: '12 месяцев',
    duration: '365 дней',
    price: 1999,
    originalPrice: 3588,
    discount: 44,
    features: [
      '🚀 Высокая скорость',
      '🌍 Все сервера',
      '📱 5 устройств',
      '💬 Поддержка 24/7',
      '🔥 Максимальная выгода',
      '🎁 Бонус: 2 месяца бесплатно',
    ],
  },
]

function App() {
  const [selectedPlan, setSelectedPlan] = useState<string | null>(null)
  const [userData, setUserData] = useState<UserData | null>(null)

  useEffect(() => {
    // Инициализация Telegram WebApp
    const tg = window.Telegram.WebApp
    tg.ready()
    tg.expand()

    // Получаем данные пользователя
    if (tg.initDataUnsafe?.user) {
      setUserData({
        id: tg.initDataUnsafe.user.id,
        firstName: tg.initDataUnsafe.user.first_name,
        lastName: tg.initDataUnsafe.user.last_name,
        username: tg.initDataUnsafe.user.username,
      })
    }

    return () => {
      tg.close()
    }
  }, [])

  useEffect(() => {
    const tg = window.Telegram.WebApp
    const mainButton = tg.MainButton

    if (selectedPlan) {
      const plan = PLANS.find((p) => p.id === selectedPlan)
      mainButton.setText(`Купить за ${plan?.price}₽`)
      mainButton.show()
      mainButton.enable()
    } else {
      mainButton.hide()
    }

    const handleClick = () => {
      if (selectedPlan && userData) {
        // Отправляем данные на бэкенд
        fetch('http://localhost:8000/api/subscriptions', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            user_id: userData.id,
            plan: selectedPlan,
          }),
        })
          .then((res) => res.json())
          .then((data) => {
            tg.showPopup({
              title: '✅ Успешно!',
              message: 'Ваша подписка активирована. Проверьте почту для получения доступа.',
              buttons: [{ type: 'ok' }],
            })
            mainButton.hide()
            setSelectedPlan(null)
          })
          .catch((err) => {
            tg.showPopup({
              title: '❌ Ошибка',
              message: 'Не удалось оформить подписку. Попробуйте позже.',
              buttons: [{ type: 'ok' }],
            })
          })
      }
    }

    mainButton.onClick(handleClick)

    return () => {
      mainButton.offClick(handleClick)
    }
  }, [selectedPlan, userData])

  const handlePlanSelect = (planId: string) => {
    setSelectedPlan(planId === selectedPlan ? null : planId)
  }

  return (
    <div className="app">
      <header className="header">
        <h1>🔐 VPN Shop</h1>
        <p className="subtitle">Быстрый и надёжный VPN</p>
      </header>

      <main className="main">
        <h2 className="plans-title">Выберите тариф</h2>

        <div className="plans">
          {PLANS.map((plan) => (
            <div
              key={plan.id}
              className={`plan-card ${selectedPlan === plan.id ? 'selected' : ''}`}
              onClick={() => handlePlanSelect(plan.id)}
            >
              {plan.discount && (
                <div className="discount-badge">-{plan.discount}%</div>
              )}

              <h3 className="plan-name">{plan.name}</h3>
              <p className="plan-duration">{plan.duration}</p>

              <div className="plan-price">
                <span className="price-current">{plan.price}₽</span>
                {plan.originalPrice > plan.price && (
                  <span className="price-original">{plan.originalPrice}₽</span>
                )}
              </div>

              <ul className="plan-features">
                {plan.features.map((feature, index) => (
                  <li key={index}>{feature}</li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      </main>

      <footer className="footer">
        <p>🛡️ Гарантия возврата денег в течение 7 дней</p>
      </footer>
    </div>
  )
}

export default App
