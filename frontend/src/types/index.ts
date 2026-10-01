declare global {
  interface Window {
    Telegram: {
      WebApp: {
        ready: () => void;
        expand: () => void;
        close: () => void;
        theme: {
          bg_color: string;
          text_color: string;
          hint_color: string;
          link_color: string;
          button_color: string;
          button_text_color: string;
        };
        initDataUnsafe: {
          user?: {
            id: number;
            first_name: string;
            last_name?: string;
            username?: string;
          };
        };
        MainButton: {
          text: string;
          color: string;
          text_color: string;
          isVisible: boolean;
          isActive: boolean;
          show: () => void;
          hide: () => void;
          enable: () => void;
          disable: () => void;
          setText: (text: string) => void;
          onClick: (callback: () => void) => void;
          offClick: (callback: () => void) => void;
        };
        onEvent: (eventType: string, eventHandler: () => void) => void;
      };
    };
  }
}

export interface SubscriptionPlan {
  id: string;
  name: string;
  duration: string;
  price: number;
  originalPrice: number;
  discount?: number;
  features: string[];
}

export interface UserData {
  id: number;
  firstName: string;
  lastName?: string;
  username?: string;
}
